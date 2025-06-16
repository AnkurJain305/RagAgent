import os
import streamlit as st
import base64
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import re

import config
from rag_agent import RagAgent
from utils.text_processing import clean_text, format_solution, parse_question
from utils.math_utils import plot_function

# Set page configuration
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .math-block {
        display: block;
        margin: 1em 0;
        text-align: center;
    }
    .math-inline {
        display: inline-block;
        vertical-align: middle;
    }
    .step-container {
        background-color: #f8f9fa;
        padding: 1em;
        border-radius: 5px;
        margin-bottom: 1em;
        border-left: 3px solid #4CAF50;
    }
    .solution-header {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'rag_agent' not in st.session_state:
    st.session_state.rag_agent = None

if 'knowledge_base_loaded' not in st.session_state:
    st.session_state.knowledge_base_loaded = False

if 'solution_history' not in st.session_state:
    st.session_state.solution_history = []

# Function to initialize the RAG agent
def initialize_agent():
    try:
        st.session_state.rag_agent = RagAgent()
        return True
    except Exception as e:
        st.error(f"Error initializing RAG agent: {str(e)}")
        return False

# Function to load the knowledge base
def load_knowledge_base():
    if st.session_state.rag_agent is None:
        if not initialize_agent():
            return False
    
    try:
        with st.spinner("Loading knowledge base..."):
            st.session_state.rag_agent.load_knowledge_base()
            st.session_state.knowledge_base_loaded = True
        return True
    except Exception as e:
        st.error(f"Error loading knowledge base: {str(e)}")
        return False

# Function to solve a question
def solve_question(question):
    if st.session_state.rag_agent is None:
        if not initialize_agent():
            return None
    
    if not st.session_state.knowledge_base_loaded:
        if not load_knowledge_base():
            return None
    
    try:
        with st.spinner("Solving the question..."):
            result = st.session_state.rag_agent.solve_question(question)
            # Add to history
            st.session_state.solution_history.append({
                "question": question,
                "solution": result["solution"],
                "plots": result.get("plots", [])
            })
            return result
    except Exception as e:
        st.error(f"Error solving the question: {str(e)}")
        return None

# Function to upload a document to the knowledge base
def upload_document(uploaded_file):
    if st.session_state.rag_agent is None:
        if not initialize_agent():
            return False
    
    try:
        # Save the uploaded file temporarily
        file_path = os.path.join("knowledge_base", uploaded_file.name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Add the document to the knowledge base
        with st.spinner("Adding document to knowledge base..."):
            success = st.session_state.rag_agent.add_document(file_path)
            if success:
                st.success(f"Document '{uploaded_file.name}' added to knowledge base.")
                st.session_state.knowledge_base_loaded = True
                return True
            else:
                st.error(f"Failed to add document '{uploaded_file.name}' to knowledge base.")
                return False
    except Exception as e:
        st.error(f"Error uploading document: {str(e)}")
        return False

# Main application UI
def main():
    # Sidebar
    with st.sidebar:
        st.title("JEE Mathematics RAG Agent")
        st.markdown("---")
        
        # Knowledge base section
        st.subheader("Knowledge Base")
        if st.button("Load Knowledge Base", key="load_kb_button"):
            load_knowledge_base()
        
        # Upload document
        st.subheader("Upload Document")
        uploaded_file = st.file_uploader("Upload a document to the knowledge base", 
                                        type=["pdf", "docx", "txt"])
        if uploaded_file is not None:
            if st.button("Add Document", key="add_doc_button"):
                upload_document(uploaded_file)
        
        # Topic selection
        st.subheader("Mathematics Topics")
        selected_topic = st.selectbox("Select a topic", config.MATH_TOPICS)
        
        # Sample questions
        st.subheader("Sample Questions")
        sample_questions = {
            "Algebra": "Solve the quadratic equation x^2 - 5x + 6 = 0.",
            "Calculus": "Find the derivative of f(x) = x^3 - 3x^2 + 2x - 1 with respect to x.",
            "Coordinate Geometry": "Find the equation of the circle passing through the points (1, 2), (3, 4), and (5, 6).",
            "Trigonometry": "Prove that sin(A+B) = sinA.cosB + cosA.sinB",
            "Vectors": "If a = 2i + 3j - k and b = i - j + 2k, find a × b.",
            "3D Geometry": "Find the shortest distance between the lines r = (1,2,3) + t(1,1,1) and r = (2,3,4) + s(2,1,0).",
            "Probability": "A bag contains 5 red balls and 3 blue balls. Two balls are drawn at random without replacement. Find the probability that both balls are of the same color.",
            "Statistics": "The mean of 100 observations is 50 and the standard deviation is 5. Find the sum of squares of all the observations.",
            "Sets and Relations": "If A = {1, 2, 3, 4, 5} and B = {4, 5, 6, 7, 8}, find A ∩ B and A ∪ B.",
            "Complex Numbers": "Find the modulus and argument of the complex number z = 3 + 4i.",
            "Matrices and Determinants": "Find the inverse of the matrix A = [[1, 2], [3, 4]].",
            "Differential Equations": "Solve the differential equation dy/dx + 2y = e^x."
        }
        
        if selected_topic in sample_questions:
            if st.button(f"Use Sample {selected_topic} Question", key=f"sample_q_{selected_topic}"):
                st.session_state.question = sample_questions[selected_topic]
        
        # History
        st.subheader("Solution History")
        for i, item in enumerate(st.session_state.solution_history):
            if st.button(f"Question {i+1}", key=f"history_{i}"):
                st.session_state.question = item["question"]
        
        # Clear history
        if st.session_state.solution_history and st.button("Clear History", key="clear_history_button"):
            st.session_state.solution_history = []
    
    # Main content area
    st.title("JEE Mathematics Problem Solver")
    st.markdown("Enter a JEE mathematics question below to get a detailed step-by-step solution.")
    
    # Question input
    if 'question' not in st.session_state:
        st.session_state.question = ""
    
    question = st.text_area("Enter your question", value=st.session_state.question, height=100)
    
    # Optional topic tag
    col1, col2 = st.columns([3, 1])
    with col2:
        add_topic_tag = st.checkbox("Add topic tag")
    
    if add_topic_tag:
        topic_tag = st.selectbox("Select the topic of your question", config.MATH_TOPICS)
        tagged_question = f"[{topic_tag}] {question}"
    else:
        tagged_question = question
    
    # Function to format solution text
    def format_solution_text(solution_text):
        # Clean up numbering and formatting
        formatted_text = solution_text.replace('**0.**', '### Analysis:')
        
        # Improve mathematical expression formatting
        formatted_text = formatted_text.replace('\\(', '<span style="font-family:serif">\\(')
        formatted_text = formatted_text.replace('\\)', '\\)</span>')
        
        # Add proper spacing and structure
        formatted_text = formatted_text.replace('- ', '<br>- ')
        formatted_text = formatted_text.replace('\n', '<br>')
        
        # Wrap in a styled div for better presentation
        formatted_text = f'''<div style="
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 1em 0;
            padding: 1em;
            background: #f8f9fa;
            border-radius: 5px;
            border-left: 4px solid #2b5876;
        ">
        {formatted_text}
        </div>'''
        
        return formatted_text
    
    # Add this CSS to your Streamlit app (in your main function):
    st.markdown("""
    <style>
    .math-solution {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 1em 0;
    }
    .math-solution h4 {
        color: #2b5876;
        margin: 1em 0 0.5em 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Solve button section - replace this part
    solve_clicked = st.button("Solve", key="solve_button")
    if solve_clicked:
        if not tagged_question.strip():
            st.warning("Please enter a question.")
        else:
            result = solve_question(tagged_question)
            if result and not result.get("error", False):
                # Display solution
                formatted_solution = format_solution_text(result["solution"])
                st.markdown("<div class='solution-header'><h2>Solution</h2></div>", unsafe_allow_html=True)
                st.markdown(formatted_solution, unsafe_allow_html=True)
                
                # Display any plots
                if "plots" in result and result["plots"]:
                    st.subheader("Graphical Representation")
                    for plot_img in result["plots"]:
                        st.image(plot_img)
    
    # Remove the second Solve button check for previous solution
    if st.session_state.solution_history:
        last_solution = st.session_state.solution_history[-1]
        st.markdown("<div class='solution-header'><h2>Previous Solution</h2></div>", unsafe_allow_html=True)
        st.markdown(f"**Question:** {last_solution['question']}")
        st.markdown(last_solution["solution"], unsafe_allow_html=True)
        
        if "plots" in last_solution and last_solution["plots"]:
            st.subheader("Graphical Representation")
            for plot_img in last_solution["plots"]:
                st.image(plot_img)

# Run the app
if __name__ == "__main__":
    main()
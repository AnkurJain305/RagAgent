import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4-turbo")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# ChromaDB configuration
CHROMA_PERSIST_DIRECTORY = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")

# RAG configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K_RETRIEVAL = 5

# Application settings
APP_TITLE = "JEE Mathematics RAG Agent"
APP_DESCRIPTION = "Solve JEE mathematics questions with detailed step-by-step solutions"

# Mathematics-specific settings
MATH_TOPICS = [
    "Algebra",
    "Calculus",
    "Coordinate Geometry",
    "Trigonometry",
    "Vectors",
    "3D Geometry",
    "Probability",
    "Statistics",
    "Sets and Relations",
    "Complex Numbers",
    "Matrices and Determinants",
    "Differential Equations"
]

# Prompt templates
QUESTION_PROMPT_TEMPLATE = """
You are an expert mathematics tutor specializing in JEE (Joint Entrance Examination) mathematics.

Question: {question}

Provide a detailed step-by-step solution to this JEE mathematics question. 
Include all mathematical reasoning, formulas, and calculations.
Format your answer with clear steps, using LaTeX notation for mathematical expressions.

Relevant information from the knowledge base:
{context}
"""
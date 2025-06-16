# JEE Mathematics RAG Agent

A Retrieval-Augmented Generation (RAG) agent designed to solve JEE (Joint Entrance Examination) mathematics questions with detailed solutions. The application features a Streamlit user interface for easy interaction.

## Features

- Solve JEE mathematics questions with step-by-step solutions
- Utilize RAG architecture for accurate and detailed answers
- Interactive Streamlit UI for question input and solution display
- Support for mathematical notation and diagrams
- Knowledge base of JEE mathematics concepts and formulas

## Setup Instructions

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```
   streamlit run app.py
   ```

## Project Structure

- `app.py`: Main Streamlit application
- `rag_agent.py`: RAG agent implementation
- `knowledge_base/`: Directory containing mathematics knowledge documents
- `utils/`: Utility functions for processing questions and formatting solutions
- `config.py`: Configuration settings

## Usage

1. Enter a JEE mathematics question in the text input field
2. Click "Solve" to generate a detailed solution
3. View the step-by-step solution with explanations

## Technologies Used

- Streamlit: For the user interface
- LangChain: For building the RAG pipeline
- OpenAI: For the language model
- ChromaDB: For vector storage
- SymPy: For symbolic mathematics
- LaTeX2MathML: For rendering mathematical notation
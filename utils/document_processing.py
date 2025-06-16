import os
import re
import pandas as pd
from typing import List, Dict, Any, Optional
from PyPDF2 import PdfReader
import docx

def read_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return ""

def read_docx(file_path: str) -> str:
    """Extract text from a DOCX file."""
    try:
        doc = docx.Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        print(f"Error reading DOCX {file_path}: {e}")
        return ""

def read_txt(file_path: str) -> str:
    """Read text from a TXT file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading TXT {file_path}: {e}")
        return ""

def read_csv(file_path: str) -> List[Dict[str, Any]]:
    """Read data from a CSV file and return as a list of dictionaries."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error reading CSV {file_path}: {e}")
        return []

def extract_document_text(file_path: str) -> str:
    """Extract text from a document based on its file extension."""
    _, ext = os.path.splitext(file_path.lower())
    
    if ext == '.pdf':
        return read_pdf(file_path)
    elif ext == '.docx':
        return read_docx(file_path)
    elif ext == '.txt':
        return read_txt(file_path)
    elif ext == '.csv':
        records = read_csv(file_path)
        # Convert CSV records to text format
        return '\n'.join([str(record) for record in records])
    else:
        print(f"Unsupported file format: {ext}")
        return ""

def extract_formulas_from_text(text: str) -> List[str]:
    """Extract mathematical formulas from text."""
    # Extract LaTeX formulas (both inline and block)
    inline_formulas = re.findall(r'\$(.*?)\$', text)
    block_formulas = re.findall(r'\$\$(.*?)\$\$', text)
    
    # Extract formulas that might be in plain text format (e.g., "f(x) = x^2 + 2x + 1")
    plain_formulas = re.findall(r'([a-zA-Z]\([a-zA-Z]\)\s*=\s*[^.\n]+)', text)
    
    return inline_formulas + block_formulas + plain_formulas

def extract_topic_from_filename(file_path: str) -> Optional[str]:
    """Extract the mathematics topic from the filename."""
    filename = os.path.basename(file_path)
    name, _ = os.path.splitext(filename)
    
    # Try to extract topic from filename
    # Example: "Calculus_Differentiation.pdf" -> "Calculus"
    parts = name.split('_')
    if len(parts) > 0:
        return parts[0]
    
    return None

def process_knowledge_document(file_path: str) -> Dict[str, Any]:
    """Process a knowledge document and extract relevant information."""
    text = extract_document_text(file_path)
    formulas = extract_formulas_from_text(text)
    topic = extract_topic_from_filename(file_path)
    
    return {
        'file_path': file_path,
        'text': text,
        'formulas': formulas,
        'topic': topic
    }
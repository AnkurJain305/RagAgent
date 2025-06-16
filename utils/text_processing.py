import re
import latex2mathml.converter as latex2mathml
from typing import Dict, List, Any

def clean_text(text: str) -> str:
    """Clean and normalize text for processing."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    # Normalize quotes
    text = re.sub(r'[''′]', "'", text)
    text = re.sub(r'["]', '"', text)
    return text

def parse_question(question: str) -> Dict[str, Any]:
    """Parse a JEE mathematics question to extract relevant information."""
    # Clean the question text
    clean_question = clean_text(question)
    
    # Extract topic if mentioned in the question
    topic_pattern = r'(?i)(algebra|calculus|coordinate geometry|trigonometry|vectors|3d geometry|probability|statistics|complex numbers|matrices)'
    topic_match = re.search(topic_pattern, clean_question)
    topic = topic_match.group(1).title() if topic_match else None
    
    # Extract mathematical expressions
    # Look for expressions like f(x) = x^2 + 2x + 1, y = mx + c, etc.
    math_expr_pattern = r'([a-zA-Z]\([a-zA-Z]\)\s*=\s*[^.\n]+|[a-zA-Z]\s*=\s*[^.\n]+)'
    math_expressions = re.findall(math_expr_pattern, clean_question)
    
    # Extract LaTeX expressions if present
    latex_pattern = r'\$(.*?)\$'
    latex_expressions = re.findall(latex_pattern, clean_question)
    
    return {
        "question": clean_question,
        "topic": topic,
        "math_expressions": math_expressions + latex_expressions
    }

def format_solution(solution_text: str) -> str:
    """Format the solution text for display."""
    # Clean the solution text
    clean_solution = clean_text(solution_text)
    
    # Convert LaTeX to MathML for better rendering
    def replace_latex(match):
        latex_expr = match.group(1)
        try:
            mathml = latex2mathml.convert(latex_expr)
            return mathml
        except:
            return f"${latex_expr}$"
    
    # Replace inline LaTeX expressions with MathML
    # solution_with_mathml = re.sub(r'\$(.*?)\$', replace_latex, clean_solution)
    
    # Format steps
    # Split by step indicators
    steps = re.split(r'(?i)(step\s*\d+:|\d+\.\s*)', clean_solution)
    formatted_steps = []
    
    for i in range(len(steps)):
        if i > 0 and re.match(r'(?i)(step\s*\d+:|\d+\.\s*)', steps[i-1]):
            # This is a step content following a step indicator
            formatted_steps.append(f"**{steps[i-1].strip()}** {steps[i].strip()}")
    
    # If no steps were found, return the original solution
    if not formatted_steps:
        return clean_solution
    
    # Join the formatted steps
    return "\n\n".join(formatted_steps)
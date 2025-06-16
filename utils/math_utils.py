import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
import base64

def solve_equation(equation_str, variable='x'):
    """Solve a mathematical equation using SymPy."""
    try:
        x = sp.Symbol(variable)
        equation = sp.sympify(equation_str)
        solution = sp.solve(equation, x)
        return solution
    except Exception as e:
        print(f"Error solving equation: {e}")
        return None

def differentiate(expression_str, variable='x'):
    """Differentiate a mathematical expression using SymPy."""
    try:
        x = sp.Symbol(variable)
        expression = sp.sympify(expression_str)
        derivative = sp.diff(expression, x)
        return derivative
    except Exception as e:
        print(f"Error differentiating expression: {e}")
        return None

def integrate(expression_str, variable='x'):
    """Integrate a mathematical expression using SymPy."""
    try:
        x = sp.Symbol(variable)
        expression = sp.sympify(expression_str)
        integral = sp.integrate(expression, x)
        return integral
    except Exception as e:
        print(f"Error integrating expression: {e}")
        return None

def plot_function(expression_str, x_range=(-10, 10), variable='x'):
    """Plot a mathematical function and return as base64 encoded image."""
    try:
        x = sp.Symbol(variable)
        expression = sp.sympify(expression_str)
        f = sp.lambdify(x, expression, 'numpy')
        
        x_vals = np.linspace(x_range[0], x_range[1], 1000)
        y_vals = f(x_vals)
        
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals)
        plt.grid(True)
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        plt.title(f'$f({variable}) = {sp.latex(expression)}$')
        plt.xlabel(variable)
        plt.ylabel(f'f({variable})')
        
        # Save plot to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format='png', dpi=100)
        plt.close()
        buf.seek(0)
        
        # Convert to base64
        img = Image.open(buf)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return f"data:image/png;base64,{img_str}"
    except Exception as e:
        print(f"Error plotting function: {e}")
        return None

def simplify_expression(expression_str):
    """Simplify a mathematical expression using SymPy."""
    try:
        expression = sp.sympify(expression_str)
        simplified = sp.simplify(expression)
        return simplified
    except Exception as e:
        print(f"Error simplifying expression: {e}")
        return None

def calculate_determinant(matrix_str):
    """Calculate the determinant of a matrix using SymPy."""
    try:
        # Convert string representation to a SymPy matrix
        # Example input: "[[1, 2], [3, 4]]"
        matrix = sp.Matrix(eval(matrix_str))
        determinant = matrix.det()
        return determinant
    except Exception as e:
        print(f"Error calculating determinant: {e}")
        return None

def calculate_eigenvalues(matrix_str):
    """Calculate eigenvalues of a matrix using SymPy."""
    try:
        matrix = sp.Matrix(eval(matrix_str))
        eigenvalues = matrix.eigenvals()
        return eigenvalues
    except Exception as e:
        print(f"Error calculating eigenvalues: {e}")
        return None
#!/usr/bin/python3
"""
This module contains a function that safely divides two numbers.
"""

def safe_divide(numerator, denominator):
    """
    Performs division and handles non-numeric inputs and division by zero.

    Args:
        numerator (str): The number to be divided.
        denominator (str): The number to divide by.

    Returns:
        str: A message with the result or an error.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        
        if den == 0:
            return "Error: Cannot divide by zero."
        
        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
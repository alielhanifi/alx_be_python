def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on user input.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform, which can be 'add', 
                         'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the arithmetic operation.
        str: An error message if division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
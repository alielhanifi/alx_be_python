num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
# match_case_calculator.py
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Error: Invalid operation."
print(f"result is: {result}")
# match_case_calculator.py
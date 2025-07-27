# 1. Define Global Conversion Factors
# These variables are in the global scope, accessible by all functions.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global factor."""
    # The formula is (F - 32) * factor
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global factor."""
    # The formula is (C * factor) + 32
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Handles user interaction, input validation, and calls conversion functions."""
    # Get and validate temperature input
    try:
        temp_str = input("Enter the temperature to convert: ")
        temperature = float(temp_str)
    except ValueError:
        # Raise an error for non-numeric input as per requirements
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Get and validate unit input
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    # Perform conversion and display the result
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Catch the specific error raised for invalid temperature and print it
        print(f"Error: {e}")
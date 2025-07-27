# Import the necessary components from the datetime module
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current date and time and displays it in a formatted string.
    """
    # Part 1: Display the Current Date and Time
    print("--- Part 1: Current Date and Time ---")
    # Save the current date and time in a variable
    current_date = datetime.now()
    
    # Format and print the current date and time
    # %Y for year, %m for month, %d for day, %H for hour, %M for minute, %S for second
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates the future date,
    and displays it.
    """
    # Part 2: Calculate a Future Date
    print("\n--- Part 2: Calculate a Future Date ---")
    while True:
        try:
            # Prompt the user to enter a number of days
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            
            # Get today's date (without the time part)
            today = datetime.now().date()
            
            # Calculate the future date using timedelta
            future_date = today + timedelta(days=days_to_add)
            
            # Print the future date
            print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
            break # Exit the loop after successful calculation
        except ValueError:
            # Handle cases where the input is not a valid integer
            print("Invalid input. Please enter a whole number for the days.")
        except Exception as e:
            # Handle other potential errors
            print(f"An error occurred: {e}")
            break

# Main execution block
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
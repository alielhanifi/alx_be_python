# daily_reminder.py

# Infinite loop to allow retry or repeated use
while True:
    # Step 1: Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Match-case based on priority
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")
            continue  # restart the loop

    # Step 3: Add time-sensitivity info
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    elif time_bound == "no":
        message += ". Consider completing it when you have free time."
    else:
        print("Invalid time-bound input. Please enter yes or no.")
        continue  # restart the loop

    # Step 4: Output reminder
    print("\nReminder:", message)
    break  # Exit after successful input and output

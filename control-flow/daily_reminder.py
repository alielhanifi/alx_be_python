# daily_reminder.py

print("--- Daily Task Reminder ---")

# Prompt for a Single Task
task = input("Enter your task: ")

# --- Input Validation for Priority ---
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# --- Input Validation for Time-bound ---
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Initialize immediate_action_message
immediate_action_message = ""

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder_prefix = f"'{task}' is a high priority task"
        if time_bound == "yes":
            immediate_action_message = " that requires immediate attention today!"
        else:
            immediate_action_message = ". Aim to complete it soon."
    case "medium":
        reminder_prefix = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            immediate_action_message = " that requires attention today."
        else:
            immediate_action_message = ". Plan to get it done."
    case "low":
        reminder_prefix = f"'{task}' is a low priority task"
        if time_bound == "yes":
            immediate_action_message = " with a deadline today."
        else:
            immediate_action_message = ". Consider completing it when you have free time."
    case _: # This case acts as a fallback, though our validation already handles it.
        reminder_prefix = f"'{task}' has an unknown priority"
        immediate_action_message = ". Please review its importance."

# Provide a Customized Reminder
print(f"Reminder: {reminder_prefix}{immediate_action_message}")

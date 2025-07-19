# daily_reminder.py

# Step 1: Gather inputs
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

# Step 2: Process using match-case
match priority:
    case "high":
        message = f"🔴 High Priority Task: {task}"
    case "medium":
        message = f"🟠 Medium Priority Task: {task}"
    case "low":
        message = f"🟢 Low Priority Task: {task}"
    case _:
        message = f"⚪ Unknown Priority Task: {task}"

# Step 3: Check if the task is time-bound
if time_bound == "yes":
    message += " – This task requires immediate attention today! ⏰"

# Step 4: Loop until user confirms task
print("\nYour Daily Reminder:")
while True:
    print(message)
    done = input("Have you completed this task? (yes to confirm): ").lower()
    if done == "yes":
        print("✅ Great job! Task marked as complete.")
        break
    else:
        print("🔁 Reminder: Don't forget to finish your task!\n")

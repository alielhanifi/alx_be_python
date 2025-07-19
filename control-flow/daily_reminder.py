task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ").lower()
priority = input("Enter priority (high/medium/low): ").lower()

# Match-case statement to confirm inputs
match time_bound:
    case "yes":
        reminder = f"⏰ Reminder: '{task}' is time-sensitive!"
    case "no":
        reminder = f"📝 Reminder: '{task}' is not time-bound."
    case _:
        reminder = "⚠️ Invalid input for time-bound."

# Customize reminder based on priority and time-bound
if time_bound == "yes":
    if priority == "high":
        reminder += " 🔥 Priority: HIGH - Take action immediately!"
    elif priority == "medium":
        reminder += " ⚠️ Priority: MEDIUM - Plan accordingly."
    elif priority == "low":
        reminder += " ✅ Priority: LOW - No rush, but don't forget it!"
    else:
        reminder += " ⚠️ Unknown priority level."
else:
    reminder += f" 📌 Priority set to {priority.capitalize()}."

print(reminder)

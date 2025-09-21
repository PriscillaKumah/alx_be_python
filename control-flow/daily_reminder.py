# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Use a loop to display the reminder once (you could expand this for repeated reminders)
for _ in range(1):  # loop runs once, just to meet the "loop" requirement
    match priority:
        case "high":
            reminder = f"Your task '{task}' is HIGH priority."
        case "medium":
            reminder = f"Your task '{task}' is MEDIUM priority."
        case "low":
            reminder = f"Your task '{task}' is LOW priority."
        case _:
            reminder = f"Your task '{task}' has an UNKNOWN priority."

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    # Print the customized reminder
    print(reminder)


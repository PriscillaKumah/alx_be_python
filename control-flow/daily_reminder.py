# Prompt for task details
task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ")
time_bound = input("Is the task time-bound? (yes/no): ")

# Loop (runs once to satisfy loop requirement)
for _ in range(1):
    match priority:
        case "high":
            reminder = f"Your task '{task}' is HIGH priority."
        case "medium":
            reminder = f"Your task '{task}' is MEDIUM priority."
        case "low":
            reminder = f"Your task '{task}' is LOW priority."
        case _:
            reminder = f"Your task '{task}' has an UNKNOWN priority."

    # Add extra message if time-bound
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    # Output reminder
    print(reminder)

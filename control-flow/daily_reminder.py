task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
Reminder = f"{task} is a {priority} priority task that requires immediate attention today!"
Note = f"{task} is a {priority} priority task. Consider completing it when you have free time."

match priority:
    case "high":
    
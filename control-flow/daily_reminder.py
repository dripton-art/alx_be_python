task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = f"{task} is a {priority} priority task that requires immediate attention today!"
note = f"{task} is a {priority} priority task. Consider completing it when you have free time."

match priority:
    case "high":
     if time_bound == "yes":
        print(f"Reminder: {reminder}")
     else:
        print(f"Note: {note}")
    case "medium":
     if time_bound == "yes":
        print(f"Reminder: {reminder}")
     else:
        print(f"Note: {note}")
    case "low":
     if time_bound == "yes":
        print(f"Reminder: {reminder}")
     else:
        print(f"Note: {note}")
    case _:
        print(f"{task} has an unknown priority. Please check your input.")
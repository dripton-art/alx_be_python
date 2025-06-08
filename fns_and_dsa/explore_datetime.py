import datetime # Importing datetime module.

def display_current_datetime():
    current_date = datetime.datetime.now().date()
    full_date = datetime.datetime.now() # full current date and time

    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    current_datetime = full_date.strftime("%Y-%m-%d %H:%M:%S") 
    print("The date today is:", current_date)
    print("Current date and time:", current_datetime)

display_current_datetime()

Days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    date = datetime.datetime.now().date()
    future_date = date + datetime.timedelta(days=Days)  
    Future_date = future_date.strftime("%Y-%m-%d")

    print("Future date:", Future_date)

calculate_future_date()
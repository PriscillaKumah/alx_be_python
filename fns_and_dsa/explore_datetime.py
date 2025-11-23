from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format it as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(current_date, days_to_add):
    # Add the number of days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date as YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future}")


def main():
    # Part 1: Display current datetime
    current_date = display_current_datetime()
    
    # Part 2: Ask user for days and calculate future date
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days)


if __name__ == "__main__":
    main()


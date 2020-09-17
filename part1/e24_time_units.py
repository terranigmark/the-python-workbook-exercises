"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
"""

def main(days, hours, minutes, seconds):
    days_to_seconds = days * 24 * 60 * 60
    hours_to_seconds = hours * 60 * 60
    minutes_to_seconds = minutes * 60
    total_seconds = days_to_seconds + hours_to_seconds + minutes_to_seconds + seconds

    return print(f"{days} days {hours} hours {minutes} minutes and {seconds} are: {total_seconds} seconds in total")

if __name__ == "__main__":
    print("This program converts the total units of time you input into seconds")
    days = int(input("How many days do you want to convert?: "))
    hours = int(input("How many hours do you want to conver?: "))
    minutes = int(input("How many seconds do you want to convert?: "))
    seconds = int(input("How many seconds do you want to add?: "))

    main(days, hours, minutes, seconds)
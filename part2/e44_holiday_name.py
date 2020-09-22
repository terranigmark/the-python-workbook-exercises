"""
Canada has three national holidays which fall on the same dates each year.
Holiday Date
New year’s day January 1
Canada day July 1
Christmas day December 25
Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.
"""

def main(canada_holidays, month, day):
    if month in canada_holidays['months'] and day in canada_holidays['days']:
        index = canada_holidays['months'].index(month)
        return print(f"That day is {canada_holidays['holidays'][index]}")
    else:
        return print("That's just another regular day...")

if __name__ == "__main__":
    canada_holidays = {
        'holidays': ['New year\'s day', 'Canada day', 'Christmas day'],
        'months': ['January', 'July', 'December'],
        'days': [1, 1, 25],
    }

    print("This program reads a date and tells you if that's a Canadian holiday.")
    month = str(input("Enter a month: ")).title()
    day = int(input("Enter a day in number: "))

    main(canada_holidays, month, day)
"""
The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise:
Season First day
Spring March 20
Summer June 21
Fall September 22
Winter December 21
Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered.
"""

def main(month, day):
    season = ''

    if month == 'January' or month == 'February':
        season = 'Winter'
    elif month == 'March':
        if day < 20:
            season = 'Winter'
        else:
            sesaon = 'Spring'
    elif month == 'April' or month == 'May':
        season = 'Spring'
    elif month == 'June':
        if day < 21:
            season = 'Spring'
        else:
            season = 'Summer'
    elif month == 'July' or month == 'August':
        season = 'Summer'
    elif month == 'September':
        if day < 22:
            season = 'Summer'
        else:
            season = 'Fall'
    elif month == 'October' or month == 'November':
        season = 'Fall'
    elif month == 'December':
        if day < 21:
            season = 'Fall'
        else:
            season = 'Winter'

    return print(f"{month} {day} is on {season}")


if __name__ == "__main__":
    print("This program reads a date and tells you what season of the year is.")
    month = str(input("Enter a month: "))
    day = int(input("Enter a day: "))

    main(month, day)
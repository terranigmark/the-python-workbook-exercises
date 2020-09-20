"""
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
"""

def main(month, thirthy_days, thirthy_one_days):
    if month.title() in thirthy_days:
        return print(f"The month {month.title()} has 30 days.")
    elif month.title() in thirthy_one_days:
        return print(f"The month {month.title()} has 31 days.")
    elif month.title() == 'February':
        return print("Sometimes February has 28 o 29 days.")
    else:
        return print("That's not a valid month...")

if __name__ == "__main__":
    thirthy_days = ['April', 'June', 'September', 'November']
    thirthy_one_days = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

    print("This program tells how many days has month.")
    month = str(input("Enter a month to know how many days has it: "))

    main(month, thirthy_days, thirthy_one_days)
"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.
"""

def main(deposit, years, interest_rate):
    interest_decimal = interest_rate / 100
    revenue = deposit * ((1 + interest_decimal) ** years)

    return print(f"If you save ${deposit} for {years} years with a compound interest of {interest_rate}% you'll get: ${round(revenue, 2)}")

if __name__ == "__main__":
    deposit = float(input("How much many will you deposit?: "))
    years = int(input("For how many years will you save it?: "))
    interest_rate = float(input("What's the yearly interest rate in percentage?: "))

    main(deposit, years, interest_rate)
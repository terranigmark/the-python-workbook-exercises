"""
It is common for images of a country’s previous leaders, or other individuals of historical significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed.
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.
Individual Amount
George Washington $1
Thomas Jefferson $2
Abraham Lincoln $5
Alexander Hamilton $10
Andrew Jackson $20
Ulysses S. Grant $50
Benjamin Franklin $100
"""

def main(banknotes, denomination):
    if denomination in banknotes['amount']:
        index = banknotes['amount'].index(denomination)
        face = banknotes['individual'][index]
        return print(f"A banknote of ${denomination} has the face of {face}.")
    else:
        return print("There are no banknotes of that denomination.")

if __name__ == "__main__":
    banknotes = {
        'individual': ['George Washington', 'Thomas Jefferson', 'Abraham Lincoln', 'Alexander Hamilton', 'Andrew Jackson', 'Ulysses S. Grant', 'Benjamin Franklin'],
        'amount': [1, 2, 5, 10, 20, 50, 100]
    }

    print("This program reads a banknote denomination and tells you if it has a famous individual face on it.")
    denomination = int(input("Enter a denomination: "))

    main(banknotes, denomination)
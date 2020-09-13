"""
This program reads a number input from the user and sums all the positives integers from 0 to n
"""

def main(number):
    sum = int((number * (number + 1)) / 2)

    return print(f"The sum of all integers from 0 to {number} are: {sum}")

if __name__ == "__main__":
    number = int(input("Input a number tu sum all the positives from zero to it: "))

    main(number)
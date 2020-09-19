"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
"""

def main(number):
    result = True

    if number % 2 == 0:
        return print(f"The number {number} is EVEN")
    else:
        return print(f"The number {number} is ODD")

if __name__ == "__main__":
    number = int(input("Enter a number to know if its even or odd: "))
    main(number)
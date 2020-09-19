"""
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
"""

def main(number):
    result = 0
    number_string = str(number)

    for i in range(len(number_string)):
        result += int(number_string[i])

    return print(f"The sum of the digits in {number_string} is: {result}")

if __name__ == "__main__":
    print("This program divides a number into digits and sums it's parts.")
    number = int(input("Enter a number to sum it's digits: "))
    main(number)
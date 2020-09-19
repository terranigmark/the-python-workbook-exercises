"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""

def main(numbers):
    return print(f'''
    The lowest number is: {min(numbers)}
    The middle number is: {max(numbers) - min(numbers)}
    The highest number is: {max(numbers)}
    ''')

if __name__ == "__main__":
    numbers = []
    print("This program reads 3 integer numbers and sort them.")

    for i in range(3):
        number = int(input("Enter a number to sort: "))
        numbers.append(number)

    main(numbers)
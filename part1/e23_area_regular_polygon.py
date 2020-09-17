"""
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:
area = n × s2 / 4 × tan(π / n)
Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.
"""
from math import tan, pi

def main(sides_lenght, sides_number):
    area = (sides_number * (sides_lenght**2)) / 4 * tan(pi / sides_number)

    return print(f"The area of a polygon with {sides_number} with a lenght of {sides_lenght} per side is: {round(area, 4)}")

if __name__ == "__main__":
    print("This program calculates the area of a regular polygon according the following information you input.")
    sides_lenght = float(input("Enter the lenght of the polygon sides: "))
    sides_number = float(input("Enter the number of the polygon sides: "))

    main(sides_lenght, sides_number)
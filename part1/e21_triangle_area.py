"""
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area = b × h / 2
Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base length b and height h.
"""

def main(base, height):
    area = (base * height) / 2

    return print(f"The area of a triangle with a base of {base} and height of {height} is: {area}")

if __name__ == "__main__":
    base = float(input("Enthe the base of a triangle to calculate it's area: "))
    height = float(input("Enter the height of the triangle to calculate it's area: "))

    main(base, height)
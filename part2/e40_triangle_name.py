"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.
"""

def main(sides):
    if (sum(sides) / 3) == sides[0]:
        return print("This is an equilateral triangle")
    elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return print("This is an isoceles triangle.")
    else:
        return print("This is a scalene triangle.")

if __name__ == "__main__":
    sides = []
    print("This program reads the lenght of 3 sides and it tells you what kind of triangle is it.")

    for i in range(3):
        sides.append(float(input(f"Enter the lenght of the side {i+1}: ")))

    main(sides)
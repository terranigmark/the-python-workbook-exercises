"""
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area = sqrt(s × (s − s1) × (s − s2) × (s − s3))
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area
"""
from math import sqrt

def main(side_1, side_2, side_3):
    sum_sides_divided = (side_1 + side_2 + side_3) / 2
    area = sqrt(sum_sides_divided * (sum_sides_divided - side_1) * (sum_sides_divided - side_2) * (sum_sides_divided - side_3))

    return print(f'''
    The triangle has a sides lenght of: {side_1}, {side_2}, {side_3}
    Thea area of the triangle is: {round(area, 4)}
    ''')

if __name__ == "__main__":
    print("This program calculates the area of a triangle based in it's sides lenght")
    side_1 = float(input("Enter the length of side 1: "))
    side_2 = float(input("Enter the length of side 2: "))
    side_3 = float(input("Enter the length of side 3: "))

    main(side_1, side_2, side_3)
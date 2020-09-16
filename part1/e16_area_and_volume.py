"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
"""
from math import pi

def main(radius):
    circle_area = pi * (radius ** 2)
    sphere_volume = (4/3 * pi) * (pow(radius, 3))

    return print(f'''
    Using a radius of {radius}...
    Circle area: {circle_area}
    Sphere volume: {sphere_volume}
    ''')

if __name__ == "__main__":
    radius = float(input("Enter a radius to calculate the area of a circle and the voulume of a sphere: "))
    main(radius)
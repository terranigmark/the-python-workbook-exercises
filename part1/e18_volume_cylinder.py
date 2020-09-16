"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
from math import pi

def main(cylinder, height):
    volume = pi * (radius ** 2) * height

    return print(f"The volume of a cylinder with a {radius} radius and {height} is: {round(volume, 2)}")

if __name__ == "__main__":
    radius = float(input("Enter a radius to calculate the volume of a cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    main(radius, height)
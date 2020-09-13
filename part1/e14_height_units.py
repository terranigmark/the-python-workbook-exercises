"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
"""

def main(feet, inches):
    feet_to_inches = feet * 12
    total_inches = inches + feet_to_inches
    inches_to_centimeters = total_inches * 2.54

    return print(f"{feet} ft and {inches} in make {total_inches} in which are {inches_to_centimeters} cm")

if __name__ == "__main__":
    feet = float(input("Enter a number of inches to convert: "))
    inches = float(input("Enter a number of inches to convert: "))

    main(feet, inches)
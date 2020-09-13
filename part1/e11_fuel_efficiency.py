"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""

def main(mpg):
    result = 235.214583 / mpg

    return print(f"{mpg} MPG are {round(result, 2)} L/100km")

if __name__ == "__main__":
    mpg = float(input("What's the MPG you want to convert to L/100km?: "))

    main(mpg)
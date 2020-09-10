"""
Program that reads the length and width of a field to calculate it's area
"""

def main():
    length = int(input("What's the length in feets of the field?: "))
    width = int(input("What's the width in feets of the field?: "))

    area_in_feets = length * width
    area_in_acres = area_in_feets / 43560

    return print(f"There are {area_in_acres} acres in the field")

if __name__ == "__main__":
    main()
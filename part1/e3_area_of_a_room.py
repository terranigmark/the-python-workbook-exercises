"""
Program that calculates the area of a room
"""

def main():
    width = float(input("What's the width of the room?: "))
    length = float(input("What's the length of the room?: "))

    area = width * length

    return print(f"The area of the room is {area} m2")

if __name__ == "__main__":
    main()
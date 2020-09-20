"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
"""

def main(sides_number, shapes):
    if sides_number < 3 or sides_number > 10:
        return print("Sorry, I'm not that smart yet...")
    elif sides_number in shapes.keys():
        return print(f"That's a {shapes.get(sides_number)}")

if __name__ == "__main__":
    shapes = {
        3: 'triangle',
        4: 'square',
        5: 'pentagon',
        6: 'hexagon',
        7: 'hptagon',
        8: 'octagon',
        9: 'nonagon',
        10: 'decagon',
    }
    print("This program reads a number and tells you the name of a regular shape with that number of sides")
    sides_number = int(input("Enter a number of sides: "))

    main(sides_number, shapes)
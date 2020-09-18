"""
In this exercise you will create a program that reads a pressure from the user in kilopascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""

def main(kpa):
    lbin2 = kpa / 6.895
    hgmm = kpa * 7.501
    atm = kpa / 101

    return print(f'''
    {kpa} kilo-pascals are equivalent to...
    lb/in2: {lbin2}
    hgmm: {hgmm}
    atm: {atm}
    ''')

if __name__ == "__main__":
    print("This program converts kilo-pascals to lb/in2, hgmm and atm. ")
    kpa = float(input("Enter the amount of kilo-pascals to convert: "))

    main(kpa)
"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
"""

def main(celsius):
    farenheit = (celsius * 9/5) + 32
    kelvin = celsius = 273.15

    return print(f'''
    {celsius} degrees Celsius are equivalent to...
    Farenheit: {farenheit} F
    Kelvin: {kelvin} K
    ''')

if __name__ == "__main__":
    print("This program convert Celsius degrees to Farenheit and Kelvin.")
    celsius = float(input("Enter a temperature in Celsius to convert: "))

    main(celsius)
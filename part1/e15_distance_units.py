"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles.
"""

def main(feet):
    ft_to_in = feet * 12
    ft_to_yd = feet * 0.33333
    ft_to_mi = feet * 0.00018939

    return print(f'''
    {feet} feet are...
    {ft_to_in} inches
    {ft_to_yd} yards
    {ft_to_mi} miles
    ''')

if __name__ == "__main__":
    feet = float(input("Enter a number of feet to convert: "))

    main(feet)
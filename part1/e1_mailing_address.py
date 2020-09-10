"""
Simple program to ask for delivery address
"""

def address():
    print("Please enter the required information.")

    name = input("Enter your name: ")
    street = input("Enter your street: ")
    number = input("Enter the number of your address: ")
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    zip_code = input("Enter your zip code: ")

    return print(f'''
    If you receive a mail or package it should be delivered to:
    {name}
    {street}
    {number}
    {city}
    {country}
    {zip_code}
    ''')


if __name__ == "__main__":
    address()
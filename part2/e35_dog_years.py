"""
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
"""

def main(human_years):
    dog_years = 0

    if human_years > 2:
        dog_years = 21 + (human_years * 4)
        return print(f"A dog of {human_years} human years old is {dog_years} dog years old.")
    else:
        dog_years = human_years * 10.5
        return print(f"A dog of {human_years} human years old is {dog_years} dog years old.")


if __name__ == "__main__":
    print("This program converts human years to dog years.")
    human_years = float(input("How many human years do you want to convert?: "))

    main(human_years)
"""
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula: BMI = (weight / height × height) × 703
If you read the height in meters and the weight in kilograms then body mass index
is computed using this slightly simpler formula: BMI = weight / (height × height)
"""

def main(height, weight):
    bmi = weight / (height**2)

    return print(f"The BMI is: {round(bmi, 2)}")

if __name__ == "__main__":
    print("This program calculates the BMI according to the following inputs.")
    height = float(input("Enter a height in meters: "))
    weight = float(input("Enter a weight in kilograms: "))

    main(height, weight)
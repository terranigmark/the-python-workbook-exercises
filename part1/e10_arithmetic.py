"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of a**b
"""

from math import log10

def main(a, b):

    sums = a + b
    difference = a - b
    product = a * b
    quotient_a = a / b
    remainder_a = a % b
    log10_a = log10(a)
    a_pow_b = a ** b

    return print(f'''
    Here are the results

    • The sum of a and b
    {sums}
    • The difference when b is subtracted from a
    {difference}
    • The product of a and b
    {product}
    • The quotient when a is divided by b
    {quotient_a}
    • The remainder when a is divided by b
    {remainder_a}
    • The result of log10 a
    {log10_a}
    • The result of a**b
    {a_pow_b}
    ''')

if __name__ == "__main__":
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    main(a, b)
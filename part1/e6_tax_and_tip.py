"""
This program calculate the tax and tip for a meal given by the user
"""

def main(meal, price):
    tip = float("{:.2f}".format(price * 0.18))
    tax = float("{:.2f}".format(price * 0.16))
    total = float("{:.2f}".format(price + tip + tax))

    return print(f'''
    Here's your bill:
    Meal:       ${meal}
    Sub-total:  ${price}
    Tip:        ${tip}
    Tax:        ${tax}

    Total:      ${total}
    ''')

if __name__ == "__main__":
    meal = input("What will be your order?: ")
    price = float(input(f"What's the price of {meal}?: "))

    main(meal, price)
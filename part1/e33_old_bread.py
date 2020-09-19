"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.
"""

def main(bread_price, discount, new_breads, old_breads):
    regular_price = bread_price * (new_breads + old_breads)
    discount_price = old_breads * discount
    total_price = regular_price - discount

    return print(f'''
    Sub-total:  ${round(regular_price, 2)}
    Discount:   ${round(discount_price, 2)}
    Total:      ${round(total_price, 2)}
    ''')

if __name__ == "__main__":
    bread_price = 3.49
    discount = 0.6

    print("This program computes the price to pay for new bread and old bread (60% OFF).")
    new_breads = int(input("How many breads of the day do you want to buy?: "))
    old_breads = int(input("How many old breads (60% OFF) do you want to buy?: "))

    main(bread_price, discount, new_breads, old_breads)
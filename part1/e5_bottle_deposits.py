"""
This program calculates a refunding depending on the size and ammount of bottles recycled
"""

def main(small_bottle_refund, big_bottle_refund):
    small_bottle_ammount = int(input("How many small bottles are you returning?: "))
    big_bottle_ammount = int(input("How many big bottles are you returning?: "))

    total_refund = (small_bottle_ammount * small_bottle_refund) + (big_bottle_ammount * big_bottle_refund)

    return print(f"You are refunded ${total_refund} for {small_bottle_ammount} small bottles and {big_bottle_ammount} big bottles.")

if __name__ == "__main__":
    small_bottle_refund = 0.10
    big_bottle_refund = 0.25

    main(small_bottle_refund, big_bottle_refund)
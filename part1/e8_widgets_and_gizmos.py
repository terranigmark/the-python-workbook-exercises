"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
"""

def main(widgets_ammount, gizmos_ammount, widgets_weight, gizmos_weight):
    total_widgets_weight = widgets_ammount * widgets_weight
    total_gizmos_weight = gizmos_ammount * gizmos_weight
    total_weight = total_gizmos_weight + total_widgets_weight

    return print(f'''
    Here's your order
    Widgets({widgets_ammount}):      {total_widgets_weight}g
    Gizmos({gizmos_ammount}):       {total_gizmos_weight}g
    Total({gizmos_ammount + widgets_ammount}):        {total_weight}g
    ''')

if __name__ == "__main__":
    widgets_weight = 75
    gizmos_weight = 112
    widgets_ammount = int(input("How many widgets will you take?: "))
    gizmos_ammount = int(input("How many gizmos will you take?: "))

    main(widgets_ammount, gizmos_ammount, widgets_weight, gizmos_weight)
"""
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row.
Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking
"""

def main(board, coordinate):
    user_column = coordinate[0]
    user_row = int(coordinate[1])
    column_index = board['columns'].index(user_column)
    row_index = board['rows'].index(user_row)

    if user_column in board['columns'] and user_row in board['rows']:
        if (column_index +1) % 2 != 0 and (row_index + 1) % 2 != 0:
            return print(f"The color of the square {coordinate} is black")
        else:
            return print(f"The color of the square {coordinate} is white")
    else:
        print("That's an invalid square")

if __name__ == "__main__":
    board = {
        'columns': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
        'rows': [1, 2, 3, 4, 5, 6, 7, 8],
    }

    print("This program reads a coordinate from a chess board and tells you what color is that square.")
    coordinate = str(input("Enter a square to know its color (e.g. e5): "))

    main(board, coordinate)
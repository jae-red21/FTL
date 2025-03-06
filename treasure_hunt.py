from random import randint
def treasure_hunt(rows, cols):
    while rows > 0:
        for _ in range(cols):
            print("*", end=" ")
        rows -= 1





def main():
    print("Welcome to the Treasure Hunt.")
    while True:
        while True:
            try:
                board_rows = int(input("Please enter number of rows for the board: "))
                board_columns = int(input("Please enter number of columns for the board: "))
                treasure_row = int(input("Choose a row to hide the treasure: "))
                treasure_column = int(input("Choose a column to hide the treasure: "))

                if board_rows < 1 or board_columns < 1:
                    raise ValueError("Input valid values")
                elif treasure_row < 1 or treasure_row > board_rows:
                    raise ValueError("Out of board bounds")
                elif treasure_column < 1 or treasure_column > board_columns:
                    raise ValueError("Out of board bounds")
                break
            except ValueError as e:
                print(f"Error: {e}. Try again.")

        treasure_hunt(board_rows, board_columns)
        response = input("Wanna play again? (y/n): ").strip().lower()[o]
        if response != "y":
            print("Thank you for playing.")
            break

if __name__ == "__main__":
    main()




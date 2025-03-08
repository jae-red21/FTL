from random import randint

def validate_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else: 
                print(f"Out of bounds, Please enter a value between {min_value} and {max_value}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
def game_board(rows, columns, hide_at_row, hide_at_column):
    print("X marks the trap and T is your treasure's location! \nHere is your board:")
    trap_row = randint(1, rows)
    trap_column = randint(1, columns)
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if i == hide_at_row and j == hide_at_column:
                if i == trap_row and j == trap_column:
                    print("X", end=" ")
                else:
                    print("T", end=" ")
            elif i == trap_row and j == trap_column:
                print("X", end=" ")
            else:
                print("*", end=" ")
        print()
        
    if hide_at_row == trap_row and hide_at_column == trap_column:
        print("\nOops, your treasure is trapped")
    else:
        print("\nWow! You're lucky your treasure wasn't trapped.")
            
        


def main():
    print("Welcome to Treasure Hunt.")
    while True:
        try: 
            rows = validate_input("Enter the number of rows for the game board (1-10): ", 1, 10)
            columns = validate_input("Enter the number of columns for the game board (1-10): ", 1, 10)
            hide_at_row = validate_input(f"Choose a row to hide the treasure (1- {rows}): ", 1, rows)
            hide_at_column = validate_input(f"Choose a column to hide the treasure (1-{columns})", 1, columns)

            game_board(rows, columns, hide_at_row, hide_at_column)
            
            play_again = input("\nWanna play again? (y/n): ").strip().lower()[0]
            if play_again != "y":
                print("Thanks for playing Treasure Hunt!")
                break
            
        except ValueError as e:
            print(f"Error: {e} Try again.")
        
        
    
if __name__== "__main__":
    main()
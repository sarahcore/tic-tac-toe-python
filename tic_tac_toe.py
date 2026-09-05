board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def show_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner():
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (
            board[combination[0]] == current_player
            and board[combination[1]] == current_player
            and board[combination[2]] == current_player
        ):
            return True

    return False

print("TIC TAC TOE")

player_x = input("Player X, enter your name: ")
player_o = input("Player O, enter your name: ")

print("\nChoose a position using the numbers below:")

print()
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")
print()

current_player = "X"

current_player = "X"

while True:

    if current_player == "X":
        current_name = player_x
    else:
        current_name = player_o

    show_board()

    print(f"{current_name}, it's your turn!")

    try:
       position = int(input("Choose a position from 1 to 9: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if position < 1 or position > 9:
        print("Please choose a number from 1 to 9!")
        continue

    if board[position - 1] == " ":
        board[position - 1] = current_player
    else:
        print("That position is already taken!")
        continue

    if check_winner():
        show_board()
        print(f"🎉 {current_name} wins!")
        break

    if " " not in board:
        show_board()
        print("It's a draw! 🤝")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
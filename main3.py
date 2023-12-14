# X_Y žaidimas
board = [" " for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def žaidėjo_ejimai(žaidėjas):
    if žaidėjas == "X":
        number = 1
    elif žaidėjas == "O":
        number = 2

    print("Jūsų eilė žaisti, žaidėjau {}".format(number))
    while True:
        try:
            choice = int(input("Įveskite savo ėjimą (1-9): ").strip())
            break
        except ValueError:
            print("Oi! Reikia įvesti skaičių nuo 1 iki 9. Pakartokite...")
   # choice = int(input("Įveskite savo ėjimą (1-9): ").strip())
    if board[choice - 1] == " ":
            board[choice - 1] = žaidėjas
            while True:
                print("Ėjimas atliktas")
                break
    else:
            while True:
                print("Ėjimas užimtas. Pakartokite!")
                return žaidėjo_ejimai(žaidėjas)



def is_victory(žaidėjas):
    if (board[0] == žaidėjas and board[1] == žaidėjas and board[2] == žaidėjas) or \
       (board[3] == žaidėjas and board[4] == žaidėjas and board[5] == žaidėjas) or \
       (board[6] == žaidėjas and board[7] == žaidėjas and board[8] == žaidėjas) or \
       (board[0] == žaidėjas and board[3] == žaidėjas and board[6] == žaidėjas) or \
       (board[1] == žaidėjas and board[4] == žaidėjas and board[7] == žaidėjas) or \
       (board[2] == žaidėjas and board[5] == žaidėjas and board[8] == žaidėjas) or \
       (board[0] == žaidėjas and board[4] == žaidėjas and board[8] == žaidėjas) or \
       (board[2] == žaidėjas and board[4] == žaidėjas and board[6] == žaidėjas):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    žaidėjo_ejimai("X")
    print_board()
    if is_victory("X"):
        print("X laimi! Sveikiname!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    žaidėjo_ejimai("O")
    if is_victory("O"):
        print_board()
        print("O laimi! Sveikiname!")
        break
    elif is_draw():
        print("It's a draw!")
        break
# X_Y žaidimas
lentelė = [" " for x in range(9)]


def print_lentelė():
    row1 = "| {} | {} | {} |".format(lentelė[0], lentelė[1], lentelė[2])
    row2 = "| {} | {} | {} |".format(lentelė[3], lentelė[4], lentelė[5])
    row3 = "| {} | {} | {} |".format(lentelė[6], lentelė[7], lentelė[8])

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
    if lentelė[choice - 1] == " ":
        lentelė[choice - 1] = žaidėjas
        while True:
            print("Ėjimas atliktas")
            break
    else:
        while True:
            print("Ėjimas užimtas. Pakartokite!")
            return žaidėjo_ejimai(žaidėjas)


def is_victory(žaidėjas):
    if (lentelė[0] == žaidėjas and lentelė[1] == žaidėjas and lentelė[2] == žaidėjas) or \
            (lentelė[3] == žaidėjas and lentelė[4] == žaidėjas and lentelė[5] == žaidėjas) or \
            (lentelė[6] == žaidėjas and lentelė[7] == žaidėjas and lentelė[8] == žaidėjas) or \
            (lentelė[0] == žaidėjas and lentelė[3] == žaidėjas and lentelė[6] == žaidėjas) or \
            (lentelė[1] == žaidėjas and lentelė[4] == žaidėjas and lentelė[7] == žaidėjas) or \
            (lentelė[2] == žaidėjas and lentelė[5] == žaidėjas and lentelė[8] == žaidėjas) or \
            (lentelė[0] == žaidėjas and lentelė[4] == žaidėjas and lentelė[8] == žaidėjas) or \
            (lentelė[2] == žaidėjas and lentelė[4] == žaidėjas and lentelė[6] == žaidėjas):
        return True
    else:
        return False


def is_draw():
    if " " not in lentelė:
        return True
    else:
        return False


while True:
    print_lentelė()
    žaidėjo_ejimai("X")
    print_lentelė()
    if is_victory("X"):
        print("X laimi! Sveikiname!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    žaidėjo_ejimai("O")
    if is_victory("O"):
        print_lentelė()
        print("O laimi! Sveikiname!")
        break
    elif is_draw():
        print("It's a draw!")
        break

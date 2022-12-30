print()
print("*" * 5, " Игра Крестики-нолики ", "*" * 5)
print()
print('Для указания ячейки используйте')
print('номер строки и номер столбца.')
print('Например: 00,  12, 21, 20 и т.д. ')

cell = []
for i in range(1, 10):
    cell.append('-')


def playing_field(cell):
    print("    " + str(0) + "  " + str(1) + "  " + str(2) + " ")
    for i in range(0, 3):
        print(" " + str(i) + " ", cell[0 + i * 3], "", cell[1 + i * 3], "", cell[2 + i * 3], " ")


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставить " + player_token + " ? ")
        if len(player_answer) != 2:
            print("Некорректный ввод.")
            continue
        try:
            coord_xy = list(map(int, list(player_answer)))
        except:
            print("Некорректный ввод.")
            continue
        if coord_xy[0] >= 0 and coord_xy[1] >= 0 and coord_xy[0] <= 2 and coord_xy[1] <= 2:
            i = coord_xy[0]
            j = coord_xy[1]
            if (str(cell[j + i * 3]) not in "XO"):
                cell[j + i * 3] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод.")


def check_win(cell):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if cell[each[0]] == cell[each[1]] == cell[each[2]]:
            return cell[each[0]]
    return False


def main(cell):
    counter = 0
    win = False
    while not win:
        playing_field(cell)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(cell)
            if tmp == 'X' or tmp == 'O':
                playing_field(cell)
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            playing_field(cell)
            print("Ничья!")
            break

main(cell)

input("Нажмите Enter для выхода!")
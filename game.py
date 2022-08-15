import random


def bot(bot_item,user_item):
    free_cells = []
    free_cells = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] != bot_item and matrix[i][j] != user_item]
    bot_item_cells = [[i,j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == bot_item]
    random.shuffle(free_cells)
    random.shuffle(bot_item_cells)
    global free_row, free_col
    for i in free_cells:
        free_row = i[0]
        free_col = i[1]
        if bot_item_cells == []:
            return [free_row,free_col]
    else:
        for i in bot_item_cells:
            bot_row = i[0]
            bot_col = i[1] 
            size = len(matrix)-1
            for i in range(len(matrix)):
                if bot_row - 1 >= 0:
                    if matrix[bot_row-1][bot_col] != bot_item and matrix[bot_row-1][bot_col] != user_item:
                        return [bot_row-1,bot_col]
                if bot_col - 1 >= 0:
                    if matrix[bot_row][bot_col-1] != bot_item and matrix[bot_row][bot_col-1] != user_item:
                        return [bot_row,bot_col-1]
                if bot_row + 1 <= size:
                    if matrix[bot_row+1][bot_col] != bot_item and matrix[bot_row+1][bot_col] != user_item:
                        return [bot_row+1,bot_col]
                if bot_col + 1 <= size:
                    if matrix[bot_row][bot_col+1] != bot_item and matrix[bot_row][bot_col+1] != user_item:
                        return [bot_row,bot_col+1]
                if bot_row + 1 <= size and bot_col + 1 <= size:
                    if matrix[bot_row+1][bot_col+1] != bot_item and matrix[bot_row+1][bot_col+1] != user_item:
                        return [bot_row+1,bot_col+1]
                if bot_row - 1 >= 0 and bot_col + 1 <= size:
                    if matrix[bot_row-1][bot_col+1] != bot_item and matrix[bot_row-1][bot_col+1] != user_item:
                        return [bot_row-1,bot_col+1]
                if bot_row + 1 <= size  and bot_col - 1 >= 0:
                    if matrix[bot_row+1][bot_col-1] != bot_item and matrix[bot_row+1][bot_col-1] != user_item:
                        return [bot_row+1,bot_col-1]
                if bot_row - 1 >= 0 and bot_col - 1 >= 0:
                    if matrix[bot_row-1][bot_col-1] != bot_item and matrix[bot_row-1][bot_col-1] != user_item:
                        return [bot_row-1,bot_col-1]
                else:
                    return [free_row, free_col]
                
def init_items():
    # user_item, bot_item
    flag = True
    while flag != False:
      user_item = input('Выберите "X" или "0"\n >> ')
      if user_item.lower() == "x":
          flag = False
          bot_item = "0"
      elif user_item.lower() == "0":
          flag = False
          bot_item = "x"
      else:
          print('Повторите')
    return user_item, bot_item

def set_cell(item,choice):
        match choice:
            case '1': matrix[0][0] = f'{item}'
            case '2': matrix[0][1] = f'{item}'
            case '3': matrix[0][2] = f'{item}'
            case '4': matrix[1][0] = f'{item}'
            case '5': matrix[1][1] = f'{item}'
            case '6': matrix[1][2] = f'{item}'
            case '7': matrix[2][0] = f'{item}'
            case '8': matrix[2][1] = f'{item}'
            case '9': matrix[2][2] = f'{item}'


def view_matrix():
    print()
    for rows in matrix:
        for i in rows:
            print(i, end = " ")
        print()

def de_coder_bot_msg(lst):
    match lst:
        case [0, 0]: return "1"
        case [0, 1]: return "2"
        case [0, 2]: return "3"
        case [1, 0]: return "4"
        case [1, 1]: return "5"
        case [1, 2]: return "6"
        case [2, 0]: return "7"
        case [2, 1]: return "8"
        case [2, 2]: return "9"


def check_cell(choice):
        match choice:
            case '1': 
                if matrix[0][0] != user_item and matrix[0][0] != bot_item:
                    return '1'
                else:
                    return False
            case '2':
                if matrix[0][1] != user_item and matrix[0][1] != bot_item:
                    return '2'
                else:
                    return False
            case '3':
                if matrix[0][2] != user_item and matrix[0][2] != bot_item:
                    return '3'
                else:
                    return False
            case '4':
                if matrix[1][0] != user_item and matrix[1][0] != bot_item:
                    return '4'
                else:
                    return False
            case '5':
                if matrix[1][1] != user_item and matrix[1][1] != bot_item:
                    return '5'
                else:
                    return False
            case '6':
                if matrix[1][2] != user_item and matrix[1][2] != bot_item:
                    return '6'
                else:
                    return False
            case '7':
                if matrix[2][0] != user_item and matrix[2][0] != bot_item:
                    return '7'
                else:
                    return False
            case '8':
                if matrix[2][1] != user_item and matrix[2][1] != bot_item:
                    return '8'
                else:
                    return False
            case '9':
                if matrix[2][2] != user_item and matrix[2][2] != bot_item:
                    return '9'
                else:
                    return False

def msg_from_user():
    flag = False
    while flag != True:
        from_user = input('Ваш ход: >> ')
        if from_user != '':
            if not check_cell(from_user):
                print('Клетка занята. Повторите!')
            else:
                flag = True
                return from_user
        else:
            print('Повторите ввод!')
        view_matrix()


def check_winner(item):
    if matrix[0][0] == item and matrix[0][1] == item and matrix[0][2] == item:
        return True
    if matrix[1][0] == item and matrix[1][1] == item and matrix[1][2] == item:
        return True
    if matrix[2][0] == item and matrix[2][1] == item and matrix[2][2] == item:
        return True
    if matrix[0][0] == item and matrix[1][0] == item and matrix[2][0] == item:
        return True
    if matrix[0][1] == item and matrix[1][1] == item and matrix[2][1] == item:
        return True
    if matrix[0][2] == item and matrix[1][2] == item and matrix[2][2] == item:
        return True
    if matrix[0][0] == item and matrix[1][1] == item and matrix[2][2] == item:
        return True
    if matrix[2][0] == item and matrix[1][1] == item and matrix[0][2] == item:
        return True

def check_tie():
    if '*' in matrix[0]:
        return True
    elif '*' in matrix[1]:
        return True
    elif '*' in matrix[2]:
        return True
    else: 
        return False
            



global matrix
matrix = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
view_matrix()
user_item, bot_item = init_items()
count = 1
while count < 11:
    print(f'Ход: {count}')
    set_cell(f'{user_item}', msg_from_user())
    view_matrix()
    print(check_winner(user_item))
    if check_winner(user_item):
        print(f'Победили: {user_item}')
        break

    if not check_tie():
        print('Ничья')
        break

    set_cell(f'{bot_item}', de_coder_bot_msg(bot(bot_item, user_item)))
    view_matrix()
    if check_winner(bot_item):
        print(f'Победили: {bot_item}')
        break

    if not check_tie():
        print('Ничья')
        break

    print()
    count += 1

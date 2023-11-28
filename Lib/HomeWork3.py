import random

# Создание пустой доски
def create_board():
    return [' ' for _ in range(9)]

# Отрисовка доски
def draw_board(board):
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')
    print()

# Ход игрока
def player_move(board, player):
    while True:
        move = int(input('Ваш ход, игрок {}: '.format(player)))
        if board[move] == ' ':
            board[move] = player
            break
        else:
            print('Неверный ход, попробуйте еще раз!')

# Проверка наличия выигрышной комбинации
def check_win(board, player):
    # Все возможные выигрышные комбинации
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],    # По горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],    # По вертикали
        [0, 4, 8], [2, 4, 6]                 # По диагонали
    ]
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Игра
def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        draw_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            draw_board(board)
            print('Игрок', current_player, 'выиграл!')
            break

        if ' ' not in board:
            draw_board(board)
            print('Ничья!')
            break

        current_player = 'O' if current_player == 'X' else 'X'
# Ход бота
def computer_move(board):
    empty_cells = [index for index, cell in enumerate(board) if cell == ' ']
    move = random.choice(empty_cells)
    board[move] = 'O'

# Игра с ботом
def play_game_with_bot():
    board = create_board()
    current_player = 'X'

    while True:
        draw_board(board)

        if current_player == 'X':
            player_move(board, current_player)
        else:
            computer_move(board)

        if check_win(board, current_player):
            draw_board(board)
            if current_player == 'X':
                print('Вы выиграли!')
            else:
                print('Бот выиграл!')
            break

        if ' ' not in board:
            draw_board(board)
            print('Ничья!')
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game_with_bot()

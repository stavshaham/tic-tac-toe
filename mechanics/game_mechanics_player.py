# game_mechanics_player - Stav Shaham
# This file contains the game mechanics for playing against another player
import gui.vsplayer as vs

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

player_turn = 'X'

# This function returns the current player's turn
def get_player_turn():
    """
    This function is responsible for getting the current player's turn.
    :return: the
    """
    global player_turn
    return player_turn

# This function updates the board
def update_board(r, c):
    """
    This function updates the board
    :param r:
    :type r: int
    :param c:
    :type c: int
    :return:
    """
    board[r][c] = player_turn
    check_win()

# This function changes the player's turn
def change_turn():
    """
    This function changes the player's turn
    :return:
    """
    global player_turn
    if (player_turn == 'X'):
        player_turn = 'O'
    else:
        player_turn = 'X'

# This function checks if the player has won
def check_win():
    """
    This function checks if the player has won
    :return: None / Player won
    """
    global board
    check_c = check_columns()
    check_r = check_rows()
    check_d = check_diagonals()
    if (check_c is not None and check_c != ''):
        vs.end_game(check_c)
        return check_c
    if (check_r is not None and check_r != ''):
        vs.end_game(check_r)
        return check_r
    if (check_d is not None and check_d != ''):
        vs.end_game(check_d)
        return check_d
    if (is_board_full()):
        vs.end_game(None)
        return None

    return None

# This function checks if the player has won in any column
def check_columns():
    """
    This function checks if the player has won in any column
    :return: None / Player won
    """
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != ''):
        return board[0][0]
    if (board[1][0] == board[1][1] and board[1][1] == board[1][2] and (board[1][0] != '' or board[1][0] != ' ')):
        return board[1][0]
    if (board[2][0] == board[2][1] and board[2][1] == board[2][2] and (board[2][0] != '' or board[2][0] != ' ')):
        return board[2][0]

    return None

# This function checks if the player has won in any row
def check_rows():
    """
    This function checks if the player has won in any row
    :return: None / Player won
    """
    if (board[0][0] == board[1][0] and board[1][0] == board[2][0] and (board[0][0] != '' or board[0][0] != ' ')):
        return board[0][0]
    if (board[0][1] == board[1][1] and board[1][1] == board[2][1] and (board[0][1] != '' or board[0][1] != ' ')):
        return board[0][1]
    if (board[0][2] == board[1][2] and board[1][2] == board[2][2] and (board[0][2] != '' or board[0][2] != ' ')):
        return board[0][2]

    return None

# This function checks if the player has won in any diagonal
def check_diagonals():
    """
    This function checks if the player has won in any diagonal
    :return: None / Player won
    """
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and (board[0][0] != '' or board[0][0] != ' ')):
        return board[0][0]
    if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and (board[2][0] != '' or board[2][0] != ' ')):
        return board[2][0]

    return None

# This function checks if the board is full or not
def is_board_full():
    """
    This function checks if the board is full
    :return:
    """
    for r in range(3):
        for c in range(3):
            if board[r][c] == ''or board[r][c] == ' ':
                return False

    return True

def reset():
    global player_turn
    global board
    player_turn = 'X'
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
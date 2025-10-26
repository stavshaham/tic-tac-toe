# game_mechanics_ai.py - Stav Shaham
# This file contains the game mechanics for playing against the ai

import gui.vsai as vs

board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

opponent = 'X'
ai = 'O'
player_turn = 'X'

# This function returns the current player's turn
def get_player_turn():
    """
    This function is responsible for getting the current player's turn.
    :return: the current player's turn
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
    if (player_turn == opponent):
        player_turn = ai
    else:
        player_turn = opponent

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
        print('a')
        vs.end_game(check_c)
        return check_c
    elif (check_r is not None and check_r != ''):
        print(check_r)
        print('b')
        vs.end_game(check_r)
        return check_r
    elif (check_d is not None and check_d != ''):
        print('c')
        vs.end_game(check_d)
        return check_d
    elif (is_board_full(board)):
        print('d')
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
def is_board_full(temp_board):
    """
    This function checks if the board is full
    :return:
    """
    for r in range(3):
        for c in range(3):
            if temp_board[r][c] == ''or temp_board[r][c] == ' ':
                return False

    return True

# This function is checking if the board is full, to be used out of the file
def global_is_board_full():
    """
    This function checks if the board is full, to be run out of the file
    :return: bool
    """
    global board
    if (is_board_full(board)):
        return True

    return False

# This function evaluates the best move possible for the AI
def evaluate():
    """
    This function evaluates the game
    :return: score
    """

    # Checks for rows X or O win
    for r in range(3):
        if (board[r][0] == board[r][1] and board[r][1] == board[r][2]):
            if (board[r][0] == ai):
                return 1
            if (board[r][0] == opponent):
                return -1

    # Checks for column X or O wins
    for c in range(3):
        if (board[0][c] == board[1][c] and board[1][c] == board[2][c]):
            if (board[0][c] == ai):
                return 1
            if (board[0][c] == opponent):
                return -1

    # Checks for diagonal X or O wins
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if (board[0][0] == ai):
            return 1
        if (board[0][0] == opponent):
            return -1

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if (board[0][2] == ai):
            return 1
        if (board[0][2] == opponent):
            return -1

    # return 0 if no one can win
    return 0

# This function plays the move using minimax algorithm
def minimax(temp_board, depth: int, is_max: bool):
    """
    This function plays the best move using minimax algorithm
    :param temp_board:
    :param depth:
    :param is_max:
    :return:
    """
    score = evaluate()

    # Checking which player has won
    if (score == 1):
        return score

    if (score == -1):
        return score

    if (is_board_full(temp_board)):
        return 0

    # AI turn
    if (is_max):
        best = -100

        # Checking all available cells.
        for r in range(3):
            for c in range(3):
                if (temp_board[r][c] == '' or temp_board[r][c] == ' '):
                    temp_board[r][c] = ai

                    # Calling the function again recursively and gets the max value
                    result = minimax(temp_board, depth + 1, not is_max)
                    best = max(best, result)
                    # Resets the board because we did not play yet
                    temp_board[r][c] = ''

        return best

    # Player turn
    else:
        best = 100
        for r in range(3):
            for c in range(3):
                if (temp_board[r][c] == '' or temp_board[r][c] == ' '):
                    temp_board[r][c] = opponent

                    # Calling the function again recursively and gets min value
                    result = minimax(temp_board, depth + 1, not is_max)
                    best = min(best, result)
                    # Resets the board because we did not play yet
                    temp_board[r][c] = ''

        return best

# This function plays returns the r, c of the best move possible
def best_move():
    """
    This function returns the best move as r, c
    :return:
    """
    best_value = -10
    best_move_possible = (-1, -1)

    for r in range(3):
        for c in range(3):
            if (board[r][c] == '' or board[r][c] == ' '):
                board[r][c] = ai

                current_value = minimax(board, 0, False)

                board[r][c] = ''

                if (best_value < current_value):
                    best_value = current_value
                    best_move_possible = (r, c)

    return best_move_possible

# This function resets the game
def reset():
    """
    This function resets the game
    :return:
    """
    global player_turn
    global board
    player_turn = 'X'
    board = [['', '', ''], ['', '', ''], ['', '', '']]
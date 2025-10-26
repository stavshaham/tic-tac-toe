# vsplayer.py - Stav Shaham
# This file contains the vs player design and algorithms

import tkinter as tk
from tkinter import messagebox
import mechanics.game_mechanics_player as gm

buttons = []

# This function handles the buttons click
def handle_click(r, c):
    """
    This function is called when a button is clicked.
    :param r:
    :param c:
    :return:
    """
    buttons[r][c].config(state=tk.DISABLED, text=f'{gm.get_player_turn()}')
    gm.update_board(r, c)
    gm.change_turn()

# This function checks if there is a winner and shows a message accordingly
def end_game(winner):
    """
    This function is called when the game ends.
    :param winner:
    :return:
    """
    if (winner is not None):
        messagebox.showinfo("Game Ended", f'Game Ended, player {winner} has won!')
    else:
        messagebox.showinfo("Game Ended", f'Game Ended, game is tied!')

    VSPlayer.cancel_buttons()


class VSPlayer(tk.Frame):

    # The initialize function, will run when we start the class (constructor)
    def __init__(self, parent, controller):
        """
        This function runs as default when calling the class.
        :param parent:
        :param controller:
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.reset_buttons()


    # This function cancels all buttons because the game is over
    @staticmethod
    def cancel_buttons():
        """
        Cancel all buttons.
        :return:
        """
        for r in range(3):
            for c in range(3):
                global buttons
                buttons[r][c].config(state=tk.DISABLED)

    # This function resets the board and the buttons to start a new game
    def restart(self):
        """
        This function restarts the game
        :return:
        """
        gm.reset()
        self.reset_buttons()

    # This function resets the view of the game
    def reset_buttons(self):
        """
        This function resets the view of the game (the buttons)
        :return:
        """
        global buttons
        buttons = []
        for r in range(3):
            row_buttons = []
            for c in range(3):
                button = tk.Button(self, text=' ', font=('Arial', 24), width=5, height=2,
                                   command=lambda r=r, c=c: handle_click(r, c))  # Placeholder for click handler
                button.grid(row=r, column=c, sticky="nsew")  # sticky makes buttons expand
                row_buttons.append(button)
            buttons.append(row_buttons)

        button = tk.Button(self, text='Quit', font=('Arial', 24), width=5, height=2,
                           command=lambda: quit())
        button.grid(row=3, column=0, sticky="nsew")
        button = tk.Button(self, text='Restart', font=('Arial', 24), width=5, height=2,
                           command=lambda: self.restart())
        button.grid(row=3, column=1, sticky="nsew")
        button = tk.Button(self, text='Home Page', font=('Arial', 24), width=5, height=2,
                           command=lambda: self.controller.show_frame("HomePage"))
        button.grid(row=3, column=2, sticky="nsew")

        # Configure the root window's grid to allow centering
        self.grid_columnconfigure(0, weight=1)  # Left padding column
        self.grid_columnconfigure(1, weight=1)  # Left padding column
        self.grid_columnconfigure(2, weight=1)  # Right padding column
        self.grid_rowconfigure(0, weight=1)  # Top padding row
        self.grid_rowconfigure(1, weight=1)  # Top padding row
        self.grid_rowconfigure(2, weight=1)  # Bottom padding row

        gm.reset()

# vsai.py - Stav Shaham
# This file contains the vs ai page design and algorithms.

import tkinter as tk
from tkinter import messagebox
import mechanics.game_mechanics_ai as gm

buttons = []

def continue_click(r, c):
    gm.update_board(r, c)
    if (not gm.global_is_board_full()):
        gm.change_turn()
        check_play()
        ai_play()

def ai_play():
    best_move = gm.best_move()
    r = best_move[0]
    c = best_move[1]
    gm.update_board(r, c)
    buttons[r][c].config(state=tk.DISABLED, text=f'{gm.get_player_turn()}')
    gm.change_turn()
    check_play()

def end_game(winner):
    if (winner is not None):
        if (winner == 'O'):
            messagebox.showinfo("Game Ended", f'Game Ended, you lost!')
        else:
            messagebox.showinfo("Game Ended", f'Game Ended, you won!')
    else:
        messagebox.showinfo("Game Ended", f'Game Ended, game is tied!')

    VSAI.cancel_buttons()

def check_play():
    player_turn = gm.get_player_turn()
    if (player_turn == 'O'):
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(state=tk.DISABLED)
    else:
        for r in range(3):
            for c in range(3):
                buttons[r][c].config(state=tk.ACTIVE)



class VSAI(tk.Frame):

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

    def handle_click(self, r, c):
        buttons[r][c].config(state=tk.DISABLED, text=f'{gm.get_player_turn()}')
        self.after(300, continue_click, r, c)

    def restart(self):
        gm.reset()
        self.reset_buttons()

    def reset_buttons(self):
        global buttons
        buttons = []
        for r in range(3):
            row_buttons = []
            for c in range(3):
                button = tk.Button(self, text=' ', font=('Arial', 24), width=5, height=2,
                                   command=lambda r=r, c=c: self.handle_click(r, c))  # Placeholder for click handler
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


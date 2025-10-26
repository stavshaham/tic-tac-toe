# home_page.py - Stav Shaham
# This file contains the home page design and algorithms.

import tkinter as tk

class HomePage(tk.Frame):

    # The initialize function, will run when we start the class (constructor)
    def __init__(self, parent, controller):
        """
        This function runs as default when calling the class.
        :param parent:
        :param controller:
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tic Tac Toe", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start Game VS AI",
                            command=lambda: controller.show_frame("VSAI"))
        button2 = tk.Button(self, text="Start Game VS Player",
                            command=lambda: controller.show_frame("VSPlayer"))
        button1.pack()
        button2.pack()

# main.py - Stav Shaham
# This file is the handler file, contains the gui view handler

# importing gui model and a message box
import tkinter as tk
from tkinter import font as tkfont
import gui.home_page as home
import gui.vsai as vsai
import gui.vsplayer as vsplayer

class Handler(tk.Tk):

    # The initialize function, will run when we start the class (constructor)
    def __init__(self, *args, **kwargs):
        """
        This function runs as default when calling the class.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title('Tic Tac Toe')

        # the container holds the frames like a stack, then the one we want to show will raise to the top
        container = tk.Frame(self)
        self.geometry("800x800")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (home.HomePage, vsai.VSAI, vsplayer.VSPlayer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """
        Show a frame for the given page name
        :param page_name: The name of the page to show
        :type page_name: str
        """
        frame = self.frames[page_name]
        frame.tkraise()
        if (page_name != "HomePage"):
            frame.reset_buttons()


if __name__ == "__main__":
    app = Handler()
    app.mainloop()
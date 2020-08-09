"""Launcher file for ALS GUI.

    @author Ryan Bender
"""

import tkinter as tk

class List_Simplifier(tk.Frame):
    """GUI for Amazon List Simplifier"""

    def __init__(self):
        """Constructor"""
        super().__init__(master=self.init_master())
        self.init_components()

    def init_master(self):
        master = tk.Tk()

        master.geometry("600x300")
        master.title("Amazon List Simplifier")
        main_icon = tk.PhotoImage(file="C:\\Users\\ryanb\\OneDrive\\Documents\\GitHub\\Amazon-List-Simplifier\\data\\main_icon.png")
        master.iconphoto(False, main_icon)

        return master


    def init_components(self):
        """Initalize components of main frame."""
        
        self.pack()


app = List_Simplifier()
app.mainloop()

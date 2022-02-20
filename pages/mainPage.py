import tkinter as tk
from tkinter import ttk

from pages.helpers.styles import LARGEFONT
from pages.unitPage import UnitPage


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid_columnconfigure(0, weight=1)
        self.controller = controller

        self.title = ttk.Label(
            self, text="Tool List", font=LARGEFONT, width=20, anchor="center"
        )
        self.unit_button = ttk.Button(
            self, text="Unit Manager", command=self.goto_unit_manager
        )

        self.title.grid(row=0, column=0, pady=10)
        self.unit_button.grid(row=1, column=0, pady=5)

    def goto_unit_manager(self):
        self.controller.show_frame(UnitPage)

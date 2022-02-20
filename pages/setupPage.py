import tkinter as tk
from tkinter import END, ttk
from pages.components.isoSelect import IsoSelect

from pages.helpers.styles import LARGEFONT, REGULAR_FONT
from pages.mainPage import MainPage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.rowconfigure(2, weight=1)

        self.label = ttk.Label(
            self,
            text="Shitty Gladius Prototype",
            font=LARGEFONT,
            width=20,
            anchor="center",
        )
        self.text_widget = self.draw_text_widget()
        self.progress_label = ttk.Label(
            self,
            text="Select an ISO to continue...",
            anchor="center",
            font=REGULAR_FONT,
        )
        self.progress = ttk.Progressbar(
            self, length=645, mode="determinate", orient="horizontal"
        )
        self.iso_select = IsoSelect(self, self.handle_progress, self.handle_done)

        self.label.grid(row=0, column=0, pady=10)
        self.text_widget.grid(row=1, column=0, padx=20)
        self.progress_label.grid(row=2, column=0, pady=5)
        self.progress.grid(row=3, column=0, pady=5)
        self.iso_select.grid(row=4, column=0, pady=10)

    def draw_text_widget(self):
        self.text_widget = tk.Text(self, width=80, height=8)
        self.text_widget.insert(END, SETUP_TEXT)
        self.text_widget.config(state="disabled", font=REGULAR_FONT)
        return self.text_widget

    def handle_progress(self, percent, label=""):
        self.progress["value"] = percent
        self.progress_label["text"] = label

    def handle_done(self):
        self.controller.show_frame(MainPage)


SETUP_TEXT = """Please move your ISO to an (ideally empty) folder so we can setup a workspace.
Once your ISO is moved click the button below and find it.

This application will not actually edit this ISO file in any way;
it will generate a separate modded ISO for you at the same location.

Oh yeah, if it's your first time it will have 4 loading bars, have fun
"""

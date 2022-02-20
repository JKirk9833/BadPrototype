import threading
import tkinter as tk
from tkinter import filedialog

from helpers.toolsHelper import setup_environment
from pages.helpers.styles import REGULAR_FONT


class IsoSelect(tk.Frame):
    def __init__(self, parent, handle_progress, handle_done=None):
        tk.Frame.__init__(self, parent)
        self.handle_progress = handle_progress
        self.handle_done = handle_done
        self.component = tk.Button(
            self, text="Select Iso", command=self.open_iso_thread, font=REGULAR_FONT
        )
        self.component.pack(side="top", fill="x")

    def open_iso_thread(self):
        threading.Thread(target=self.select_iso).start()

    def select_iso(self):
        filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select a File",
            filetypes=(("Iso files", "*.iso*"), ("all files", "*.*")),
        )
        setup_environment(filename, self.handle_progress)
        self.handle_done()

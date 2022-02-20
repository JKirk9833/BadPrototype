import os
import tkinter as tk
from helpers.finders.fileFinder import get_iso_name
from helpers.managers.ConfigManager import ConfigManager
from pages.mainPage import MainPage
from pages.setupPage import StartPage
from pages.unitPage import UnitPage


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(row=0, column=0)

        self.frames = {}

        for F in (StartPage, MainPage, UnitPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_remove()

        last_workspace = ConfigManager().read("last_workspace")
        if bool(last_workspace) == True:
            if self.check_valid_workspace(last_workspace):
                return self.show_frame(MainPage)
            else:
                self.remove_last_workspace()
        self.show_frame(StartPage)

    def show_frame(self, cont):
        for fme in self.frames:  # Remove all frames
            self.frames[fme].grid_remove()
        frame = self.frames[cont]
        frame.grid()

    def remove_last_workspace(self):
        config = ConfigManager().read()
        config["last_workspace"] = ""
        ConfigManager().replace(config)

    def check_valid_workspace(self, ws_path):
        if not os.path.isdir(ws_path):
            return False
        iso = get_iso_name(ws_path)

        if iso == None:
            return False
        else:
            iso_name = iso.split(".")[0]
            dir_contents = os.listdir(ws_path)
            modded_dir_name = f"{iso_name}_MODDED"
            vanilla_dir_name = f"{iso_name}_VANILLA"
            for file in dir_contents:
                if file == modded_dir_name:
                    modded_dir_name = True
                if file == vanilla_dir_name:
                    vanilla_dir_name = True
            if modded_dir_name and vanilla_dir_name:
                return True
            else:
                return False


if __name__ == "__main__":
    app = tkinterApp()
    app.title("Hi there! I'm a terrible prototype!")
    app.resizable(False, False)
    app.mainloop()

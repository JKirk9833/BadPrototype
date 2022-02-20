import os
from helpers.managers.ConfigManager import ConfigManager


def get_iso_name(ws_path=None, extension=True):
    iso_dir = ws_path or ConfigManager().read("last_workspace")
    dir_contents = os.listdir(iso_dir)
    for file in dir_contents:
        if file.endswith(".iso"):
            if extension == False:
                return file.split(".iso")[0]
            return file
    return None

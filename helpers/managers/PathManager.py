import pathlib
import sys


class PathManager:
    def __init__(self):
        # The main.py directory path
        self.exec_path = pathlib.Path(sys.modules["__main__"].__file__).parent

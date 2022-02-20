import json
import os

from helpers.managers.PathManager import PathManager


class ConfigManager:
    def __init__(self):
        self.config_path = f"{PathManager().exec_path}/config.json"

    # If there is no config file, it will generate one with the provided iso at the last_workspace
    # If there is a config file but it is invalid json, it will replace it with the above
    # If there is a config file it will update the workspace with the ws_dir
    def setup(self, ws_dir):
        if not os.path.isfile(self.config_path):
            config_dict = {"last_workspace": ws_dir}
            with open(self.config_path, "w") as f:
                json.dump(config_dict, f, ensure_ascii=False, indent=2)
        else:
            try:
                with open(self.config_path) as f:
                    new_config = json.load(f)
                    new_config["last_workspace"] = ws_dir
                    json.dump(new_config, f, ensure_ascii=False, indent=2)
            except:
                print(
                    "[setup_config] ERROR: JSON in config invalid, regenerating file."
                )
                os.remove(self.config_path)
                self.setup(ws_dir)

    # If no key provided it will return the entire document as a dict
    # If a key is provided, the value of the key will be returned or an empty dict if invalid
    def read(self, key=None):
        if not os.path.isfile(self.config_path):
            return ""

        try:
            with open(self.config_path) as f:
                if key == None:
                    return json.load(f)
                return json.load(f)[key]
        except:
            print("[read_config] ERROR: JSON in config invalid, regenerating file.")
            os.remove(self.config_path)

    # Will write the new_config dict (replaces the old configuration)
    def replace(self, new_config):
        with open(self.config_path, "w") as f:
            json.dump(new_config, f, ensure_ascii=False, indent=2)

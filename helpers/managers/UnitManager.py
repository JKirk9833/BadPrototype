from collections import namedtuple
import math
import pathlib
from helpers.finders.fileFinder import get_iso_name
from helpers.managers.ConfigManager import ConfigManager

Unit = namedtuple(
    "Unit", "unit_bytes school name unit_class outfit tint skills stats items"
)

# UNITS ARE ALL IN ALPHABETICAL ORDER NO MATTER WHAT PLEASE
# OTHERWISE I CAN'T MAP SYMBOLS TO NAMES EFFICIENTLY

# Actually, since we have GB's of RAM
class UnitManager:
    def __init__(self):
        self.last_workspace = ConfigManager().read("last_workspace")
        self.iso_name = get_iso_name(extension=False)
        self.unit_dir = (
            f"{self.last_workspace}/{self.iso_name}_MODDED/gladius_bec/data/units/"
        )
        self.schools = f"{self.unit_dir}unitschools.idx"
        self.names = f"{self.unit_dir}unitnames.idx"
        # Harvest classdefs.tok for the id's / names for unitclasses.idx
        # For now I'll just populate it with the ID from unitunits.idx
        self.skills = f"{self.unit_dir}unitskills.idx"
        self.stats = f"{self.unit_dir}unitstats.idx"
        self.items = f"{self.unit_dir}unititems.idx"
        self.units = f"{self.unit_dir}unitunits.idx"  # No CD byte unlike the others
        self.unit_count = math.ceil(self.get_size(self.units) / 14) - 1

    def load_unit_index(self):
        units = []
        with open(self.units, "rb") as units_file:
            with open(self.names) as names_file:
                names_file.read(1)  # CD byte read so it's not included as a string
                for i in range(self.unit_count):
                    unit_data = units_file.read(14)
                    unit_name = self.read_unit_name(names_file)
                    units.append(self.create_unit(unit_data, unit_name))
        return units

    def read_unit_name(self, names_file):
        name_str = ""
        while True:
            byte = names_file.read(1)
            if byte == "" or bytes(byte, "utf-8") == bytes("\x00", "utf-8"):
                break
            else:
                name_str += byte
        return name_str

    # Provide hex value for unit_name e.g. Unit.name.hex()
    def get_unit_name(self, unit_name):
        unit_offset = int.from_bytes(unit_name, "big")
        with open(self.names) as f:
            f.read(1)
            string_count = 0
            string_store = ""
            byte_store = []
            while True:
                byte = f.read(1)
                if byte == "" or string_count == int(unit_offset):
                    break
                if bytes(byte, "utf-8") == bytes("\x00", "utf-8"):
                    byte_store.append(string_store)
                    string_store = ""
                    string_count += 1
                else:
                    string_store += byte
            return byte_store[len(byte_store) - 1]

    def create_unit(self, unit_data, unit_name):
        return Unit(
            unit_data,
            unit_data[0:2],  # School
            unit_name,  # Name
            unit_data[4:5],  # Class
            unit_data[5:6],  # Outfit
            unit_data[6:8],  # Tint
            unit_data[8:10],  # Skills
            unit_data[10:12],  # Stats
            unit_data[12:14],  # Items
        )

    def get_size(self, path):
        return pathlib.Path(path).stat().st_size

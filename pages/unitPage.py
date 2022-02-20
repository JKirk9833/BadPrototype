import tkinter as tk
from tkinter import ttk
from helpers.managers.UnitManager import UnitManager

from pages.helpers.styles import LARGEFONT


class UnitPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.unit_manager = UnitManager()
        self.title = ttk.Label(
            self, text="Unit Manager", font=LARGEFONT, width=20, anchor="center"
        )
        self.render_table()

        self.title.grid(row=0, column=0, pady=10)

    def render_table(self):
        table = ttk.Treeview(self, height=20)
        scroll = tk.Scrollbar(self, command=table.yview)
        scroll.grid(row=1, column=2, sticky="ns")
        table.configure(yscrollcommand=scroll.set)
        columns = [
            "school",
            "name",
            "class",
            "outfit",
            "tintset",
            "skillset",
            "statset",
            "itemset",
        ]
        self.assign_columns(table, columns)
        self.assign_data(table)
        table.grid(row=1, column=1)

    def assign_columns(self, table, columns):
        table["columns"] = columns
        # Create dummy column
        table.column("#0", width=0, stretch="no")
        table.heading("#0", text="", anchor="center")
        sizes = {
            "school": 100,
            "name": 100,
            "class": 80,
            "outfit": 60,
            "tintset": 80,
            "skillset": 80,
            "statset": 80,
            "itemset": 80,
        }
        for name in columns:
            table.column(name, width=sizes[name])
            table.heading(name, text=name.capitalize())

    def assign_data(self, table):
        units = self.unit_manager.load_unit_index()
        for i in range(self.unit_manager.unit_count):
            unit = units[i]
            table.insert(
                parent="",
                index="end",
                values=(
                    unit.school,
                    unit.name,
                    unit.unit_class,
                    unit.outfit,
                    unit.tint,
                    unit.skills,
                    unit.stats,
                    unit.items,
                ),
            )

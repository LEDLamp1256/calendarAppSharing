import tkinter as tk
from tkinter import ttk

import main


class Event(ttk.Frame):
    def __init__(self, name: str, time: str, superwidget : tk.Widget):
        super(Event, self).__init__(superwidget)
        self.name = name
        self.time = time

        timeLabel = ttk.Label(self, text = time)
        timeLabel.grid(column = 0, row = 10)

        descriptionLabel = ttk.Label(self, text = name)
        descriptionLabel.grid(column = 10, row = 10)

        ttk.Button(self, text="Delete", command= self.deleteEvent).grid(column=20, row=10)


    def deleteEvent(self):
        self.grid_remove()
        #main.saveDay()
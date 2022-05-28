import tkinter as tk
from tkinter import ttk


class Event(ttk.Frame):
    def __init__(self, name: str, time: str, superwidget : tk.Widget, fullscreen = True):
        super(Event, self).__init__(superwidget)
        self.name = name
        self.time = time

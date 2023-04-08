import tkinter as tk
from tkinter import ttk



class Event(ttk.Frame):
    def __init__(self, name: str, time: str, superwidget : tk.Widget, onDeleteFunction, googleCalendar = True):
        super(Event, self).__init__(superwidget)
        self.name = name
        self.time = time
        self.onDeleteFunction = onDeleteFunction
        self.googleCalendar = googleCalendar

        timeLabel = ttk.Label(self, text = time)
        timeLabel.grid(column = 0, row = 10)

        descriptionLabel = ttk.Label(self, text = name)
        descriptionLabel.grid(column = 10, row = 10)

        ttk.Button(self, text="Delete", command= self.deleteEvent).grid(column=20, row=10)


    def deleteEvent(self):
        self.grid_remove()
        self.onDeleteFunction()
        #main.saveDay()

class EventParent():
    def __init__(self, name, time, googleCalendar = True):
        self.name = name
        self.time = time
        self.googleCalendar = googleCalendar

    #takes in superwidget & ondelete, uses name, time, google cal value to return new event
    def eventCreate(self, superwidget, ondelete):
        return Event(self.name, self.time, superwidget, ondelete, self.googleCalendar)

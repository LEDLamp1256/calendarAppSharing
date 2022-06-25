import tkinter as tk
import calendar
from typing import Dict, List

import event
from event import Event
from tkinter import ttk, NSEW
import datetime

#todo find out google classroom importing stuff
#work on iterating through calendar output
#figure out idea for end result (what is the desired outcome)
#persistence in program(.json)

dayStorage:Dict[datetime.datetime,List[Event]] = {}
root = tk.Tk()
frame = tk.Frame(root, padx=10, pady=10 )
frame.config()
frame.grid()
ttk.Label(frame, text = "Month").grid(column = 10, row = 0)

daysofmonth = tk.Frame(frame, padx=10, pady=10)
#daysframe = ttk.Frame(frame, padding=10)
#daysframe.grid(column = 10, row = 20)
daysofweek = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
for i in range(7):
    tk.Label(daysofmonth, text = daysofweek[i], width = 5, height = 2).grid(column = i, row = 0, padx = 2, pady = 2)
#ttk.Button(frame, text = "Exit button", command = root.destroy).grid(column = 10, row = 20)

dayViewFrame = ttk.Frame(frame, padding=10)
dayViewFrame.grid(column = 100 , row = 30)
innerFrameEvents = ttk.Frame(dayViewFrame, padding = 10)
innerFrameEvents.grid(column =0 , row =0)
innerFrameCreation = ttk.Frame(dayViewFrame, padding = 10)
innerFrameCreation.grid(column = 0, row = 1)
placeholder1 = Event("placeholder1", "12:00", dayViewFrame)
placeholder2 = Event("placeholder2", "13:00", dayViewFrame)
placeholder3 = Event("placeholder3", "14:00", dayViewFrame)
eventList = [placeholder1, placeholder2, placeholder3]

def addEvent(time, name):
    addEvent = Event(name, time, innerFrameEvents)
    addEvent.grid()

editDayStorage = None

def editDay(event):
    global editDayStorage
    print(event.widget.datetimestorage)
    print(editDayStorage)
    date = event.widget.datetimestorage
    print(dayStorage)
    innerFrameEvents.winfo_children()
    dayStorage[editDayStorage] = []
    for child in innerFrameEvents.winfo_children():
        if editDayStorage is not None and "in" in child.grid_info():
            dayStorage[editDayStorage].append(child)
            print(child.grid_info())
        child.grid_remove()
    eventList = dayStorage.get(date, [])
    print(dayStorage)
    print(eventList)
    for idx, i in enumerate(eventList):
        i.grid(column = 0, row = 0 + idx, sticky = NSEW)
        print(i)
    eventList.clear()
    timeEntry = tk.StringVar()
    timeEntry.set("00:00")
    ttk.Entry(innerFrameCreation, textvariable=timeEntry).grid(column = 0, row = 0)
    nameEntry = tk.StringVar()
    nameEntry.set("placeholder name")
    ttk.Entry(innerFrameCreation, textvariable=nameEntry).grid(column = 1, row = 0)
    ttk.Button(innerFrameCreation, text = "Add Event", command = lambda: addEvent(timeEntry.get(), nameEntry.get())).grid(column = 2, row = 0)
    editDayStorage = date
    print(dayStorage)
    print()
    # tk.Label(dayViewFrame, text = event).grid(column = 100, row = 0, padx = 2, pady = 2)
#daysofmonth = tk.Frame(frame, padx=10, pady=10)
daysofmonth.grid(column=10, row=30)
daysofmonth.config(background = "grey")
cal = calendar.TextCalendar(calendar.MONDAY)
year = 2022
month = 6
cal.formatmonth(year, month)
print(cal.formatmonth(year, month))
for idx, day in enumerate(cal.itermonthdays(year, month)):
    if day == 0:
        pass
    else:

        lbl = tk.Label(daysofmonth, text=day, width = 5, height = 5)
        lbl.grid(column=idx%7, row=idx//7 + 10, padx = 2, pady = 2)
        lbl.datetimestorage = datetime.datetime(year, month, day)
        lbl.bind("<Button-1>", lambda e: editDay(e))
print(day)
root.mainloop()

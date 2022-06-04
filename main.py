import tkinter as tk
import calendar
import event
from event import Event
from tkinter import ttk, NSEW

#todo find out google classroom importing stuff
#work on iterating through calendar output
#figure out idea for end result (what is the desired outcome)
#persistence in program(.json)

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
placeholder1 = Event("placeholder1", "12:00", dayViewFrame)
placeholder2 = Event("placeholder2", "13:00", dayViewFrame)
placeholder3 = Event("placeholder3", "14:00", dayViewFrame)
eventList = [placeholder1, placeholder2, placeholder3]
def editDay(event, dayNumber):
    print(eventList)
    for idx, i in enumerate(eventList):
        i.grid(column = 10, row = 0 + idx, sticky = NSEW)
        print(i)

    #tk.Label(dayViewFrame, text = event).grid(column = 100, row = 0, padx = 2, pady = 2)

#daysofmonth = tk.Frame(frame, padx=10, pady=10)
daysofmonth.grid(column=10, row=30)
daysofmonth.config(background = "grey")
cal = calendar.TextCalendar(calendar.MONDAY)
cal.formatmonth(2022, 5)
print(cal.formatmonth(2022, 5))
for idx, i in enumerate(cal.itermonthdays(2022, 5)):
    if i == 0:
        pass
    else:
        lbl = tk.Label(daysofmonth, text=i, width = 5, height = 5)
        lbl.grid(column=idx%7, row=idx//7 + 10, padx = 2, pady = 2)
        lbl.bind("<Button-1>", lambda e: editDay(e, i))
root.mainloop()

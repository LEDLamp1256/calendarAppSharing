import tkinter as tk
import calendar
from tkinter import ttk

#todo find out google classroom importing stuff
#work on iterating through calendar output
#figure out idea for end result (what is the desired outcome)
#persistence in program(.json)

root = tk.Tk()
frame = tk.Frame(root, padx=10, pady=10 )
frame.config()
frame.grid()
ttk.Label(frame, text = "Month").grid(column = 10, row = 10)

daysofmonth = tk.Frame(frame, padx=10, pady=10)
daysframe = ttk.Frame(frame, padding=10)
daysframe.grid(column = 10, row = 20)
daysofweek = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
for i in range(7):
    tk.Label(daysofmonth, text = daysofweek[i], width = 5, height = 2).grid(column = i, row = 0, padx = 2, pady = 2)
#ttk.Button(frame, text = "Exit button", command = root.destroy).grid(column = 10, row = 20)

dayViewFrame = ttk.Frame(frame, padding=10)
dayViewFrame.grid(column = 100 , row = 0)
def editDay(event, dayNumber):
    tk.Label(dayViewFrame, text = event).grid(column = 100, row = 0, padx = 2, pady = 2)

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

import tkinter
import calendar
from tkinter import ttk

#todo find out google classroom importing stuff
#work on iterating through calendar output
#figure out idea for end result (what is the desired outcome)
#persistence in program(.json)

root = tkinter.Tk()
frame = ttk.Frame(root, padding=10 )
frame.grid()
ttk.Label(frame, text = "Month").grid(column = 10, row = 10)
daysframe = ttk.Frame(frame, padding=10)
daysframe.grid(column = 10, row = 10)
daysofweek = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
for i in range(7):
    ttk.Label(daysframe, text = daysofweek[i]).grid(column = i, row = 20)
#ttk.Button(frame, text = "Exit button", command = root.destroy).grid(column = 10, row = 20)
cal = calendar.TextCalendar(calendar.MONDAY)
cal.formatmonth(2022, 5)
print(cal.formatmonth(2022, 5))
root.mainloop()

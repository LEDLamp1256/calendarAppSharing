import tkinter as tk
import calendar
from typing import Dict, List
import classroomapi
import event
from event import Event
from tkinter import ttk, NSEW
import datetime
import json
from customJson import DictionaryEncoder, DictionaryDecoder



#figure out idea for end result (what is the desired outcome)

dayStorage:Dict[datetime.datetime,List[Event]] = {}
root = tk.Tk()
frame = tk.Frame(root, padx=10, pady=10 )
frame.config()
frame.grid()
monthscrollerframe = tk.Frame(frame)
monthscrollerframe.grid(column = 1, row = 0)
monthlabel = ttk.Label(monthscrollerframe, text = "month")
monthlabel.grid(column = 10, row = 0)
monthscrollbuttonleft = ttk.Button(monthscrollerframe, text = "<-")
monthscrollbuttonright = ttk.Button(monthscrollerframe, text = "->")
monthscrollbuttonleft.grid(column = 0, row = 0)
monthscrollbuttonright.grid(column = 11, row = 0)

upcomingEvents = tk.Frame(frame, padx = 10, pady = 10)
upcomingEvents.grid(column = 0, row = 1)
upcomingEventsTitle = ttk.Label(frame, text = "Upcoming events")
upcomingEventsTitle.grid(column = 0, row = 0)

daysofmonth = tk.Frame(frame, padx=10, pady=10)
#daysframe = ttk.Frame(frame, padding=10)
#daysframe.grid(column = 10, row = 20)
daysofweek = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
for i in range(7):
    tk.Label(daysofmonth, text = daysofweek[i], width = 5, height = 2).grid(column = i, row = 0, padx = 2, pady = 2)
#ttk.Button(frame, text = "Exit button", command = root.destroy).grid(column = 10, row = 20)

dayViewFrame = ttk.Frame(frame, padding=10)
dayViewFrame.grid(column = 2 , row = 1)
innerFrameEvents = ttk.Frame(dayViewFrame, padding = 10)
innerFrameEvents.grid(column = 0, row =0)
innerFrameCreation = ttk.Frame(dayViewFrame, padding = 10)
innerFrameCreation.grid(column = 0, row = 1)
eventList = []

previousDay : datetime.datetime = None

def saveDay():


    global previousDay

    if previousDay is not None:
        dayStorage[previousDay] = []
        for child in innerFrameEvents.winfo_children():
            if "in" in child.grid_info():
                dayStorage[previousDay].append(child)
        monthslider(previousDay.year, previousDay.month)


    curDay = datetime.date.today()

    cal = calendar.TextCalendar(calendar.MONDAY)
    for child in upcomingEvents.winfo_children():
        child.destroy()
    ttk.Label(upcomingEvents, text = "Events in the next 3 days:").grid()
    daysAhead = 8
    for idx, day in enumerate(cal.itermonthdays(curDay.year, curDay.month)):
        if day >= curDay.day and daysAhead > 0:
            daysAhead -= 1
            if daysAhead == 3:
                ttk.Label(upcomingEvents, text = "Events in the next 5 days:").grid()
            if daysAhead == 1:
                ttk.Label(upcomingEvents, text = "Events in the next 7 days:").grid()

            upcomingEventsDateTime = datetime.datetime(curDay.year, curDay.month, day)
            for e in dayStorage.get(upcomingEventsDateTime, []):
                ttk.Label(upcomingEvents, text = f"{e.time}, {e.name}").grid()


    print("Saving day.")

    #checking next month so calendar loop over
    nextYear = curDay.year
    nextMonth = curDay.month + 1

    if nextMonth == 13:
        nextMonth = 1
        nextYear += 1
    for idx, day in enumerate(cal.itermonthdays(nextYear, nextMonth)):
        if daysAhead > 0:
            daysAhead -= 1
            if daysAhead == 3:
                ttk.Label(upcomingEvents, text = "Events in the next 5 days:").grid()
            if daysAhead == 1:
                ttk.Label(upcomingEvents, text = "Events in the next 7 days:").grid()
            upcomingEventsDateTime = datetime.datetime(nextYear,nextMonth, day)
            for e in dayStorage.get(upcomingEventsDateTime, []):
                ttk.Label(upcomingEvents, text=f"{e.time}, {e.name}").grid()
        else:
            break

with open("calendarAppInfo.json", "r") as saveFile:
    temp = json.load(saveFile, cls = DictionaryDecoder)
    print(temp)
    for date in temp:
        print(temp[date])
        newKey = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        eventOnly = []
        for x in temp[date]:
            if x is not None:
                eventOnly.append(x.eventCreate(innerFrameEvents, saveDay))
        dayStorage[newKey] = eventOnly

courselist = classroomapi.getclasses()
courseidinuse = []
for course in courselist:
    if course["courseState"] == "ACTIVE" :
        courseidinuse.append(course["id"])



for courseid in courseidinuse:
        if "courseWork" in (courseworkstorage := classroomapi.classroomgetassignment(courseid)):
            activecoursework = courseworkstorage["courseWork"]
            for assignment in activecoursework:
                print(assignment)
                if "dueDate" in assignment:
                    if "dueTime" in assignment:
                        if "minutes" in assignment["dueTime"]:
                            utcduedate = datetime.datetime(assignment["dueDate"]["year"], assignment["dueDate"]["month"]
                                                           ,
                                                       assignment["dueDate"]["day"], assignment["dueTime"]["hours"],
                                                       assignment["dueTime"]["minutes"], tzinfo=datetime.timezone.
                                                       utc)
                        else:
                            utcduedate = datetime.datetime(assignment["dueDate"]["year"], assignment["dueDate"]["month"]
                                                           ,
                                                       assignment["dueDate"]["day"], assignment["dueTime"]["hours"],
                                                       0, tzinfo=datetime.timezone.
                                                       utc)
                    else:
                        raise Exception("duedate w no duetime")
                        utcduedate = datetime.datetime(assignment["dueDate"]["year"], assignment["dueDate"]["month"],
                                                       assignment["dueDate"]["day"], 23, 59, tzinfo=datetime.timezone.
                                                       utc)
                    localduedate = utcduedate.replace(tzinfo = datetime.timezone.utc).astimezone(None)
                    #     assignmentduetimestring = ""
                    #     if "hours" in assignment["dueTime"]:
                    #         assignmentduetimestring += str(assignment["dueTime"]["hours"]) + ":"
                    #     else:
                    #         assignmentduetimestring += "23:"
                    #     if "minutes" in assignment["dueTime"]:
                    #         assignmentduetimestring += str(assignment["dueTime"]["minutes"])
                    #     else:
                    #         assignmentduetimestring += "00"
                    # else:
                    #     assignmentduetimestring = "23:59"
                    duedate = datetime.datetime(localduedate.year, localduedate.month, localduedate.day)

                    duedateevent = Event(assignment["title"], f"{localduedate.hour}:{localduedate.minute if localduedate.minute > 9 else '0' + str(localduedate.minute)}", innerFrameEvents, saveDay)
                    if duedate in dayStorage:
                        dayStorage[duedate].append(duedateevent)
                    else:
                        dayStorage[duedate] = [duedateevent]


def addEvent(time, name, googleCalendarTF):
    newEvent = Event(name, time, innerFrameEvents, saveDay, googleCalendar = googleCalendarTF)
    print(newEvent.googleCalendar)
    newEvent.grid()
    saveDay()




def editDay(event):
    global previousDay
    print(event.widget.datetimestorage)
    print(previousDay)
    date:datetime.datetime = event.widget.datetimestorage
    print(dayStorage)
    #eventList = dayStorage.get(date, [])
    #eventList.clear()
    if previousDay is not None:
        dayStorage[previousDay] = []
    for child in innerFrameEvents.winfo_children():
        if previousDay is not None and "in" in child.grid_info():
            dayStorage[previousDay].append(child)
            print(child.grid_info())
        child.grid_remove()
    eventList = dayStorage.get(date, [])
    for idx, i in enumerate(eventList):
        i.grid(column = 0, row = 0 + idx, sticky = NSEW)
        print(i)
    timeEntry = tk.StringVar()
    timeEntry.set("00:00")
    ttk.Entry(innerFrameCreation, textvariable=timeEntry).grid(column = 0, row = 0)
    nameEntry = tk.StringVar()
    nameEntry.set("placeholder name")
    ttk.Entry(innerFrameCreation, textvariable=nameEntry).grid(column = 1, row = 0)
    ttk.Button(innerFrameCreation, text = "Add Event", command = lambda: addEvent(timeEntry.get(), nameEntry.get(), googleCalendarTF=False)).grid(column = 2, row = 0)
    previousDay = date
    print(dayStorage)
    print()
    monthslider(date.year, date.month)
    # tk.Label(dayViewFrame, text = event).grid(column = 100, row = 0, padx = 2, pady = 2)
#daysofmonth = tk.Frame(frame, padx=10, pady=10)
daysofmonth.grid(column=1, row=1)
daysofmonth.config(background = "grey")

currentday = datetime.datetime.today()


year = currentday.year
month = currentday.month

monthdictionary = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}



def monthslider(year, month):
    curDay = datetime.date.today()
    cal = calendar.TextCalendar(calendar.MONDAY)
    cal.formatmonth(year, month)
    print(cal.formatmonth(year, month))
    monthlabel.config(text = f"It is {monthdictionary[month]}, {year}")
    for child in daysofmonth.winfo_children():
        child.destroy()
    daysofweek = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    for i in range(7):
        tk.Label(daysofmonth, text=daysofweek[i], width=5, height=2).grid(column=i, row=0, padx=2, pady=2)
    for idx, day in enumerate(cal.itermonthdays(year, month)):
        if day == 0:
            pass
        else:
            lbl = tk.Label(daysofmonth, text=day, width=5, height=5)
            lbl.grid(column=idx % 7, row=idx // 7 + 10, padx=2, pady=2)
            lbl.datetimestorage = datetime.datetime(year, month, day)
            lbl.bind("<Button-1>", lambda e: editDay(e))
            print(lbl.datetimestorage)
            print(dayStorage.get(lbl.datetimestorage, []))
            r = 245
            g = 230
            b = 66
            if len(dayStorage.get(lbl.datetimestorage, [])) == 0:
                lbl.config(bg = f"#{r :02x}{g :02x}{b :02x}")
            else:
                g -= 20 * len(dayStorage.get(lbl.datetimestorage, []))
                g = max(g, 0)
                lbl.config(bg = f"#{r :02x}{g :02x}{b :02x}")
            if curDay == lbl.datetimestorage.date():
                lbl.config(bg = "lightblue")


def monthscrollerleft():
    global month
    global year
    month -= 1

    if month == 0:
        month = 12
        year -= 1
    monthslider(year, month)

def monthscrollerright():
    global month
    global year
    month += 1

    if month == 13:
        month = 1
        year += 1
    monthslider(year, month)

monthscrollbuttonleft.config(command = monthscrollerleft)
monthscrollbuttonright.config(command = monthscrollerright)

saveDay()
monthslider(currentday.year, currentday.month)
root.mainloop()


with open("calendarAppInfo.json", "w") as saveFile:
    jsonDumpKeys = {}
    for i in dayStorage:
        jsonDumpKeys[str(i)] = dayStorage[i]
    json.dump(jsonDumpKeys, saveFile, cls = DictionaryEncoder)
print("placeholer")

#Timetable for becarios UNIOVI - Ing Informatica

from event import Event

internship = "tatin"
timetableFile = ".\horario.txt"
timetableFileCSV = ".\horario.csv"

def readFile(fileName):
    f= open(timetableFile,"r")
    return f.readlines()

def parseHour(time, dateTime):
    n = 0
    hour = []
    for c in time:
        hour.append(c)
        n = n+1

    if len(time) == 3:
        stringHour = hour[0] + "." + hour[1] + hour[2]
    else:
        stringHour =  hour[0] + hour[1] + "." + hour[2] + hour[3]

    return stringHour

def parseNextHour(time, dateTime):
    stringHour = ""
    if(time.split(".")[1] == "30"):
        stringHour += str(int(time.split(".")[0]) + 1) + ".00"
    else:
        stringHour += time.split(".")[0] + ".30"

    return stringHour

def processLine(line):
    event = "Becaria" #event name  
    date = line.split(".append")[0].split('"')[1].replace("#", "").replace("_a", "")
    eventDay = date.split("_")[0].split("-")
    eventHour = date.split("_")[1]
    dateTime = eventDay[2] + "/" + eventDay[1] + "/" + eventDay[0]
    startHour = parseHour(eventHour, dateTime)
    endHour = parseNextHour(startHour, dateTime)
    return Event(event, dateTime, startHour, dateTime, endHour)

"""
This funtion is for return a dict with a array of events.
Return example: {
    '19/02/2019' : [Event, Event, Event],
    '20/02/2019' : [Event, Event, Event]
}
"""
def splitEventsInArrayOfDays(events):
    #TODO
    return events

"""
Events is a list of events from only one day, this funtions should
merge events if is continue.
"""
def mergeContinueEvents(events):
    #TODO
    return events

def get(timetable):
    text = "Subject, Start Date, Start Time, End Date, End Time,  Description\n"
    for line in timetable:
        if internship in line:
            text += processLine(line).toString() + "\n"
    return text

def createFile(file, linesFormatted):
    text_file = open(file, "w")
    text_file.write(linesFormatted)
    text_file.close()

#Principal method.
print(" ** Converting file " + timetableFile + " to csv file... **")
createFile(timetableFileCSV, get(readFile(timetableFile)))
print(" ** FINISH! You will find in " + timetableFileCSV + " **")


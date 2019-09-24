#Timetable for becarios UNIOVI - Ing Informatica

from event import Event
import webrequest

isNextWeek = True
user = "tuUser"
password = "tuPass"
timetableFileCSV = ".\horario.csv"

# def readFile(fileName):
#     f= open(timetableFile,"r")
#     return f.readlines()

def readWeb(user, password, isNextWeek):
    return webrequest.autologin(user, password, isNextWeek)

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
Check if there are any events that start at the same time.
"""
def checkIfEventIsInAList(event, events):
    for e in events:
        if e.startHour == event.startHour:
            return True
    return False

"""
This funtion is for return a dict with a array of events.
Return example: {
    '19/02/2019' : [Event, Event, Event],
    '20/02/2019' : [Event, Event, Event]
}
"""
def splitEventsInArrayOfDays(events):
    dic = {}
    for event in events:
        if event.startDate in dic.keys():
            dic[event.startDate].append(event)
        else:
            dic[event.startDate] = []
            dic[event.startDate].append(event)
    return dic

"""
Events is a list of events from only one day, this funtions should
merge events if is continue.
"""
def mergeContinueEvents(events):
    mergedEvents = []
    firstIteration = True
    for event in events:
        #If is first iteration
        if firstIteration:
            startHour = event.startTime
            endHour = event.endTime
            firstIteration = False

        else:
            if event.startTime == endHour:
                endHour = event.endTime
            else:
                mergedEvents.append(Event(event.subject, event.startDate, startHour, event.endDate, endHour))
                startHour = event.startTime
                endHour = event.endTime
    mergedEvents.append(Event(event.subject, event.startDate, startHour, event.endDate, endHour))
        
    return mergedEvents

def get(timetable):
    #All list of event
    eventList = []
    for unprocessed in timetable:
        line = unprocessed.decode("utf-8")
        if user in line:
            eventList.append(processLine(line))

    #Process dic with days
    eventFinalList = []
    dic = splitEventsInArrayOfDays(eventList)
    for key in dic:
        for event in mergeContinueEvents(dic[key]):
            eventFinalList.append(event)

    text = "Subject, Start Date, Start Time, End Date, End Time,  Description\n"
    for event in eventFinalList:
        text += event.toString() + "\n"
    return text

def createFile(file, linesFormatted):
    text_file = open(file, "w")
    text_file.write(linesFormatted)
    text_file.close()

#Principal method.
print(" ** Loading web and processing to csv file... **")
createFile(timetableFileCSV, get(readWeb(user, password, isNextWeek)))
print(" ** FINISH! You will find in " + timetableFileCSV + " **")

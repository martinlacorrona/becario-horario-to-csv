# Prueba python

internship = "tatin"
timetableFile = ".\horario.txt"
timetableFileCSV = ".\horario.csv"

def readFile(fileName):
    f= open(timetableFile,"r")
    return f.readlines()

def parseHours(time, dateTime):
    n = 0
    hour = []
    for c in time:
        hour.append(c)
        n = n+1

    if len(time) == 3:
        stringHour = hour[0] + "." + hour[1] + hour[2]
    else:
        stringHour =  hour[0] + hour[1] + "." + hour[2] + hour[3]

    stringHour += "," + dateTime ##End date

    if(stringHour.split(".")[1] == "30"):
        stringHour += "," + str(int(stringHour.split(".")[0]) + 1) + ".00"
    else:
        stringHour += "," + stringHour.split(".")[0] + ".30"

    return stringHour

def processLine(line):
    event = "Becaria," #event name  
    date = line.split(".append")[0].split('"')[1].replace("#", "").replace("_a", "")
    eventDay = date.split("_")[0].split("-")
    eventHour = date.split("_")[1]
    dateTime = eventDay[2] + "/" + eventDay[1] + "/" + eventDay[0]
    event += eventDay[2] + "/" + eventDay[1] + "/" + eventDay[0] + ","
    event += parseHours(eventHour, dateTime)
    return event

def get(timetable):
    text = "Subject, Start Date, Start Time, End Date, End Time,  Description\n"
    for line in timetable:
        if internship in line:
            text += processLine(line) + "\n"
    return text

def createFile(file, linesFormatted):
    text_file = open(file, "w")
    text_file.write(linesFormatted)
    text_file.close()

#Principal method.
print(" ** Converting file " + timetableFile + " to csv file... **")
createFile(timetableFileCSV, get(readFile(timetableFile)))
print(" ** FINISH! You will find in " + timetableFileCSV + " **")


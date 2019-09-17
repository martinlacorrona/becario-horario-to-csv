class Event:
    def __init__(self, subject, startDate, startTime, endDate, endTime):
        self.subject = subject
        self.startDate = startDate
        self.startTime = startTime
        self.endDate = endDate
        self.endTime = endTime

    def toString(self):
        return self.subject + ", " + self.startDate + ", " + self.startTime + ", " + self.endDate + ", " + self.endTime
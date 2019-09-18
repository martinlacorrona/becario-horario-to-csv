from event import Event

events = [
    Event("BecariaTest", "18/09/2019" , "9.00", "18/09/2019", "9.30"),
    Event("BecariaTest", "19/09/2019" , "9.30", "19/09/2019", "10.00"),
    Event("BecariaTest", "20/09/2019" , "10.00", "19/09/2019", "10.30"),
    Event("BecariaTest", "10/09/2019" , "11.00", "20/09/2019", "11.30"),
    Event("BecariaTest", "20/09/2019" , "11.30", "21/09/2019", "12.00"),
    Event("BecariaTest", "18/09/2019" , "12.00", "20/09/2019", "12.30"),
    Event("BecariaTest", "18/09/2019" , "12.30", "18/09/2019", "13.00")
]

def createdic(events):
    dic = {}
    for event in events:
        if event.startDate in dic.keys():
            dic[event.startDate].append(event)
        else:
            dic[event.startDate] = []
            dic[event.startDate].append(event)
    return dic
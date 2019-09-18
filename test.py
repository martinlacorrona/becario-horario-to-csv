events = [
    Event("BecariaTest", "18/09/2019" , "9.00", "18/09/2019", "9.30"),
    Event("BecariaTest", "18/09/2019" , "9.30", "18/09/2019", "10.00"),
    Event("BecariaTest", "18/09/2019" , "10.00", "18/09/2019", "10.30"),
    Event("BecariaTest", "18/09/2019" , "11.00", "18/09/2019", "11.30"),
    Event("BecariaTest", "18/09/2019" , "11.30", "18/09/2019", "12.00"),
    Event("BecariaTest", "18/09/2019" , "12.00", "18/09/2019", "12.30"),
    Event("BecariaTest", "18/09/2019" , "12.30", "18/09/2019", "13.00")
]
for e in splitEventsInArrayOfDays(events):
    print(e.toString())
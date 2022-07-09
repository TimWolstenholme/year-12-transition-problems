import re
from xml.dom.pulldom import END_DOCUMENT
class Event:
 
    def __init__(self,date:str,start_time:str,end_time:str) -> None:
        self.date=date
        self.start_time=start_time
        self.end_time=end_time



def menu():
    pass
def create_event():
    date=input("What is the date of the event, please use the format dd/mm/yyyy ")
    format="^(((0[1-9]|[12][0-9]|30)[-/]?(0[13-9]|1[012])|31[-/]?(0[13578]|1[02])|(0[1-9]|1[0-9]|2[0-8])[-/]?02)[-/]?[0-9]{4}|29[-/]?02[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$"
    while not re.match(format,date):
        date=input("Please enter the date in the correct format, dd/mm/yyyy ")
    while True:
        start_time=input("What is the start time of the event")
        try:
            int(start_time)
        except TypeError:
            print("Please enter a number in the format hhmm ")
            continue
        if len(start_time)<4 or int(start_time)>2399 or int(end_time[2:])>59:
            print("Please enter a number 0000<=number<2400 where the final 2 digits are in the range 00<=number<60 ")
        else:
            break

    while True:
        end_time=input("What is the finish time of the event ")
        try:
            int(end_time)
        except TypeError:
            print("Please enter a number in the format hhmm ")
            continue
        if len(end_time)<4 or int(end_time)>2399 or int(end_time[2:])>59:
            print("Please enter a number 0000<=number<2400 where the final 2 digits are in the range 00<=number<60 ")
        else:
            break
    event=Event(date,start_time,end_time)
    return event

        
def check_calendar():
    pass
def commit_event(event):
    pass
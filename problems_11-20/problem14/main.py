import re
import json
from time import sleep
class Event:
 
    def __init__(self,date:str,start_time:str,end_time:str) -> None:
        self.date=date
        self.start_time=start_time
        self.end_time=end_time



def menu():
    sleep(1)
    print("Option 1 = Create new event \n Option 2 = Search for a specific event \n Option 3 = See all events \n Option 4 = quit")
    while True:
        try:
            option=int(input("Which option do you want "))
        except: 
            print("Please enter an integer")
            continue
        if option<1 or option >4:
            print("Please enter a number in the range 0<n<5")
        else:
            break
    create_event() if option==1 else search_for_event() if option==2 else print_all() if option==3 else quit()


def create_event()->Event:
    name=input("What is the name of the event ")
    date=input("What is the date of the event, please use the format dd/mm/yyyy ")
    format="^(((0[1-9]|[12][0-9]|30)[/](0[13-9]|1[012])|31[-/]?(0[13578]|1[02])|(0[1-9]|1[0-9]|2[0-8])[-/]?02)[-/]?[0-9]{4}|29[-/]?02[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$"
    while not re.match(format,date) and not '-' in list(date):
        date=input("Please enter the date in the correct format, dd/mm/yyyy ")
    while True:
        start_time=input("What is the start time of the event ")
        try:
            int(start_time)
        except TypeError:
            print("Please enter a number in the format hhmm ")
            continue
        if len(start_time)<4 or int(start_time)>2399 or int(start_time[2:])>59:
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
    return event,name

        
def check_calendar(event:Event)->bool:
    with open('events.json','r+') as f:
        arr=f.readline()
        i=0
        events=[]
        while True:
            try:
                events.append(json.loads(json.loads(arr)[i]))
            except IndexError:
                break
            i+=1
    for item in events:
        data:dict=next(iter(item.values()))[1]
        if event.date==data["date"] and ((int(event.start_time)>data["start_time"] and int(event.start_time)<data["end_time"]) or int(event.end_time)>data["start_time"] and int(event.end_time)<data["end_time"] ):
            reject=input(f"This event clashes with {next(iter(item.keys()))[1]} do you want to cancel adding this event? (y/n) ")
            while reject.lower()[0]!='y' and reject.lower()[0]!='n':
                reject=input("Please use the format y/n ")
            reject=False if reject.lower()[0]=='y' else True
            return reject



def commit_event():
    event,name=create_event()
    
    reject=check_calendar(event)
    if reject:
        print("Event cancelled")
        menu()
    json_object=json.dumps({name:event.__dict__})
    with open('events.json','r+') as f:
        data=json.load(f)
        data.append(json_object)
        f.seek(0)
        json.dump(data,f)
    menu()
    
def search_for_event():
    name=input("What is the name of the event you are searching for ")
    with open('events.json','r+') as f:
        arr=f.readline()
        i=0
        events=[]
        while True:
            try:
                events.append(json.loads(json.loads(arr)[i]))
            except IndexError:
                break
            i+=1
    found=False
    for element in events:
        if name in list(element.keys()):
            print(json.dumps(element, sort_keys=False, indent=4))
            found=True
            break
    if not found:
        print("That event does not exist")
    menu()




def print_all():
    with open('events.json','r+') as f:
        arr=f.readline()
        i=0
        events=[]
        while True:
            try:
                events.append(json.loads(json.loads(arr)[i]))
            except IndexError:
                break
            i+=1
    print(json.dumps(events, sort_keys=False, indent=4))
    menu()

if __name__=='__main__':
    menu()


    



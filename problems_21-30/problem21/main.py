from ast import dump
from json import dumps, load


def write_to_file(id,arr):
    with open('members.json','r+')as f :
        json_object=dumps({id:arr})
        data=load(f)
        data.append(json_object)
        f.seek(0)
        dump(data,f)






while True:
    name=input("What is your firstname")
    surname=input("What is your surname")
    id=input("What is your membership ID")
    print(f"First Name: \n {name}")
    print(f"Surname: \n {surname}")
    print(f"Membership ID \n {id}")
    confirm =input("Is this correct? (y/n) ")
    if confirm.lower()=='y':
        write_to_file(id,[name,surname])
        repeat=input("Do you want to enter another username(y/n) ")
        if repeat.lower()=='y':
            continue
        break



    
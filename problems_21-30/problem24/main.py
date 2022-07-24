from secrets import choice
from string import printable


chars=list(printable)
password=[]
for i in range(10):
    password.append(choice(chars))
password=''.join(char for char in password)
pword=input("What do you think the password is : ")
if pword !=password:
    print("Incorrect Password")
else:
    with open("secret-file.txt","r+") as f:
        file_contents=f.readlines()
    for line in file_contents:
        print(line)
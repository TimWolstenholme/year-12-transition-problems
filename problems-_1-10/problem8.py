#3 different tables, called class1, class2, class3
'''
|studentID | firstname | surname | score1 | score2 | score3 |



'''

from mysql import connector
from random import randint
from primePy.primes import check
db=connector.connect(
    host='localhost',
    user='root',
    password='mypassword [not my real password]',
    database='problem8'
    
)
db_cursor=db.cursor()
firstname=input("Enter your first name ")
surname=input("Enter your surname ")
class_number=int(input("What class are you in 1/2/3 "))
score=0
for i in range(10):
    num1=randint(1,100)
    num2=randint(1,100)
    operation=randint(1,4)
    if operation==1:
        answer=int(input(f"{num1} + {num2}"))
        if answer==num1+num2:
            score+=1
            print("Correct")
        else:
            print(f"Incorrect \n The answer is {num1 + num2}")
    elif operation==2:
        answer=int(input(f"{num1} - {num2}"))
        if answer==num1-num2:
            score+=1
            print("Correct")
        else:
            print(f"Incorrect \n The answer is {num1 - num2}")
    elif operation==3:
        answer=int(input(f"{num1} * {num2}"))
        if answer==num1*num2:
            score+=1
            print("Correct")
        else:
            print(f"Incorrect \n The answer is {num1 * num2}")
    else:
        while num1%num2!=0 and num1>num2:
            if not check(num1):
                num1=randint(1,100)
            num2=randint(1,100)
        answer=int(input(f"{num1}/{num2} "))
        if answer==num1/num2:
            score +=1
            print("Correct")
        else:
            print(f"Incorrect \n The answer is {num1 / num2}")
print(f"Your score is {score}")
if class_number==1:
    class_code="class1"
elif class_number==2:
    class_code='class2'
else:
    class_code='class3'

db_cursor.execute(f"SELECT COUNT(*) FROM {class_code} WHERE firstname='{firstname} and surname= {surname} ';")
num=db_cursor.fetchmany()
db_cursor.close()
db_cursor=db.cursor()
if num[0][0]:
    db_cursor.execute(f"UPDATE {class_code} SET score3=score2, score2=score1, score1={score} where firstname={firstname} and surname={surname}")
else:
    db_cursor.execute(f"INSERT INTO {class_code} (firstname, surname, score1) VALUES( '{firstname}', '{surname}', {score})")
db.commit()


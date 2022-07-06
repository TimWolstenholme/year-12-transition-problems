from random import randint
questions=[]
answers=[]
with open("questions.txt",'r') as f:
    for line in f:
        question,answer=line.split('-')
        questions.append(question)
        answers.append(answer)
quiz_answers=[]
for i in range(1,11):
    idx=randint(0,49)
    quiz_answers.append(answers[idx])
    x=input(f"Question {i}: \n {questions[idx]} (press enter to continue)")
for i in range(1,11):
    x=input(f"Answer {i}: {quiz_answers[i]} (press enter to continue)")


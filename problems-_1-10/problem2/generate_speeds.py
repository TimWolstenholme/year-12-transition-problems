import random
with open('problem2data.txt','a')as f:
    numberplate=[]
    for i in range(2):
        numberplate.append(chr(random.randint(65,90)))
    for i in range(2):
        numberplate.append(str(random.randint(1,10)))
    numberplate.append(" ")
    for i in range(3):
        numberplate.append(chr(random.randint(65,90)))
    numberplate=''.join(element for element in numberplate)
    speed=str(random.randint(40,75))
    f.write(numberplate +'_'+speed+'\n')
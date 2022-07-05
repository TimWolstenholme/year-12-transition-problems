#find first 8 happy numbers#
def is_happy(n):
    seen=set()
    while True:
        if n==1:    return True
        elif n in seen:     return False
        else:
            seen.add(n)
            n=sum(int(i)**2 for i in str(n))

happy_numbers=[]
num=1
while len(happy_numbers)<8:
    if is_happy(num):
        happy_numbers.append(num)
    num+=1
print(happy_numbers)

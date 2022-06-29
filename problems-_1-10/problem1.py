#factorial finder

def iterative_factorial(num):
    sum=1
    for i in range(1,num+1):
        sum*=i
    return sum
def recursive_factorial(num,sum=1):
    if num==0:
        return sum
    return recursive_factorial(num-1,sum*num)
print(iterative_factorial(6))

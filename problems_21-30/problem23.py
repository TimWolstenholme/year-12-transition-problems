import numpy as np
numbers=int(input("How many digits of the fibonacci sequence do you want? "))
nums=[]
n1,n2=1,1
nums.append(n1)
nums.append(n2)
print(n1, end=" ")
print(n2, end=" ")
for i in range(numbers-2):
    n1,n2=n1+n2,n1
    print(n1, end=" ")
    nums.append(n1)
print("\n Sequence reversed: ")
print(*(num for num in np.flip(nums)))
print(f"Sum = {np.sum(nums)}")



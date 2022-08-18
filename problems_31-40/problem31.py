import numpy as np
string=input("What is the input: ")
if list(string)==list(np.flip(list(string))):
    print("Palindrome")
else:
    print("Not palindrome")
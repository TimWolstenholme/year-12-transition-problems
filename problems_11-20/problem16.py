from math import ceil, log10
def is_kaprekar(n):
    digits=ceil(log10(n))
    n_squared=n**2
    if ceil(log10(n_squared))==2*digits:
        if int(str(n_squared)[:digits])+int(str(n_squared)[digits:])!=n:
            return False
        else:
            return True
    else:
        if int(str(n_squared)[:digits-1])+int(str(n_squared)[digits-1:])!=n:
            return False
        else:
            return True
n=int(input("What is the integer"))
print(is_kaprekar(n))
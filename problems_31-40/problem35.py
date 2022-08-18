from random import randint
from primePy import primes
num=randint(1,30)
print(f"number is {num}")
multiplier=1
if num%2==0:
    multiplier*=2
if num%10==0:
    multiplier*=3
if primes.check(num):
    multiplier*=5
if num<5:
    multiplier*=2
print(multiplier if multiplier !=1 else 0)
numbers=[]
while True:
    try:
        num=int(input("Enter your number, enter a string to quit: "))
    except ValueError:
        break
    numbers.append(num)
numbers.sort()
print(numbers)
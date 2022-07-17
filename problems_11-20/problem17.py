n=int(input("How large do you want the square to be (n*n) "))
symbol=int(input("Option 1 = +, Option 2 = * Option 3 = - Option 4 = / , please enter number 1-4 "))
if symbol==2:
    for row in range(1, n + 1):
        print(*(f"{row*col:3}" for col in range(1, n + 1)))
elif symbol==1:
    for row in range(0, n + 1):
        print(*(f"{row+col:3}" for col in range(0, n + 1)))
elif symbol==3:
    for row in range(0, n + 1):
        print(*(f"{row-col:3}" for col in range(0, n + 1)))
elif symbol==4:
    print("1.0  2.0  3.0  4.0")
    for row in range(2, n + 1):
        print(*(f"{round(row/col,2)} " for col in range(1, n + 1)))
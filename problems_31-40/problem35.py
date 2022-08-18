side1=int(input("What is the length of shortest side: "))
side2=int(input("What is the length of the second longest side "))
side3=input("What is the length of the longest side: ")
if side1+side2<=side3:
    print("That isn't a triangle")
else:
    if side1==side2==side3:
        print("Equilateral")
    elif side1==side2 or side1==side3 or side2==side3:
        print("isosceles")
    else:
        print("scalene")
    if side1**2+side2**2==side3**2:
        print("Right angled")
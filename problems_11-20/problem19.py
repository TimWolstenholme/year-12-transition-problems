print("What is the gate which is being entered")
gate=input("Please write OR, AND, XOR,NOR, NAND in capitals")
n1=int(input("What is the first input"))
n2=int(input("What is the second input"))
if gate.upper()=="OR":
    print(n1 or n2)
elif gate.upper()=="AND":
    print(n1 and n2)
elif gate.upper()=="XOR":
    print(n1^n2)
elif gate.upper()=="NOR":
    print(not (n1 or n2))
elif gate.upper()=="NAND":
    print(not (n1 and n2))
else:
    print("Invalid gate")
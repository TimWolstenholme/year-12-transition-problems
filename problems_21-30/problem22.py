def tax():
    income=int(input("What is your yearly income"))
    return 0.2*income if income>37701 else 0.4*income if income<150001 else 0.45*income
def vat():
    price=float(input("What is the price without VAT"))
    return round(price*1.2,2)
def times_table():
    n1=int(input("Enter the first number"))
    n2=int(input("Enter the second number"))
    return n1*n2
while True:
    print("Option 1: tax \n Option 2: vat \n Option 3: multiplication ")
    option=input("Please enter an integer in the range 1-3 to choose your options, if anything else is inputted the program will quit ")
    if option=='1':
        tax()
    elif option=='2':
        vat()
    elif option=='3':
        times_table()
    else:
        break

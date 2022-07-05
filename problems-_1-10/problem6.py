#convertion calculator
#Converts between celcius and farenheit, pints and litres, ounces and grams



class WrongUnitError(Exception):
    def __init__(self,unit1,unit2 ) -> None:
        self.message=f"{unit1} cannot be converted into {unit2} "
        super().__init__(self.message)

c_to_f=lambda c:c*1.8 + 32
f_to_c=lambda f:(f-32)/1.8
pints_to_litres=lambda p:p/1.76
litres_to_pints=lambda l:l*1.76
oz_to_g=lambda oz:oz*28.35
g_to_oz=lambda g:g/28.35
units=['celcius','farenheit','pints','litres','grams','ounces']
convertable={'celcius':'farenheit','pints':'litres','grams':'ounces'}
print(units)
u1=input("What is the unit of the quantity you have")
while u1 not in units:
    print("Please only input a unit in the above list")
    u1=input("What is the unit of the quantity you have")
quantity=input("What is the quantity")
u2=input("What is the unit of the quantity you want to convert to")
while u2 not in units:
    print("Please only input a unit in the above list")
    u2=input("What is the unit of the quantity you want to convert to")
for key,value in zip(convertable):
    if u1==key and u2==value or u2==key and u1==value:
        valid=True
if not valid:
    raise WrongUnitError(u1,u2)
if u1=='celcius':
    farenheit=c_to_f(quantity)
    print(f"{farenheit} degrees farenheit")
elif u1=='farenheit':
    celcius=f_to_c(quantity)
    print(f"{celcius} degrees celcius")
elif u1=='pints':
    litres=pints_to_litres(quantity)
    print(f"{litres} litres")
elif u1=='litres':
    pints=litres_to_pints(quantity)
    print(f"{pints} pints")
elif u1=='grams':
    ounces=g_to_oz(quantity)
    print(f"{ounces} ounces")
else:
    grams=oz_to_g(quantity)
    print(f"{grams} grams")
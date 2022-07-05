from secrets import choice


symbols=['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']
money=1
play=True
while play and money>0.2:
    money-=0.2
    symbol_1=choice(symbols)
    symbol_2=choice(symbols)
    symbol_3=choice(symbols)
    print(f"Symbol 1 is {symbol_1} \n Symbol 2 is {symbol_2} \n Symbol 3 is {symbol_3}")
    if symbol_1==symbol_2==symbol_3:
        print(f"You won {1 if symbol_1 !='Bell' else 5}")
        money+=1 if symbol_1!='Bell' else 5
    elif (symbol_1==symbol_2) ^ (symbol_2==symbol_3)  ^ (symbol_1==symbol_3):
        print("You won 50p")
        money+=0.5
    else:
        print("You lose")
        money=round(money,2)
    print(f"Your money is £{money}0")
    repeat=input("Do you want to play again (Y/N)? ")
    while repeat.upper()!='Y' and repeat.upper() !='N':
        repeat=input("Do you want to play again (Y/N)? ")
    if repeat.upper()=='N':
        play=False


print(f"Your money is £{money}0")
      
    
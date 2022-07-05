from inflect import engine
p=engine()
number=float(input("What is the number you want to convert to words  "))
number=int(number) if int(number)==number else float(number)
print(p.number_to_words(number)) 
from unicodedata import numeric


num_to_letter={1:['A','B','C'],2:['D','E','F'],3:['G','H','I'],4:['J','K','L'],5:['M','N','O'],6:['P','Q','R'],7:['S','T','U'],8:['V','W','X'],9:['Y','Z']}
section1,section2,section3=input("Please write your phone number in the format 000-ABC-DEFG: ").split('-')
section1=list(section1)
section2=list(section2)
section3=list(section3)
numerical_s2=[]
numerical_s3=[]
for letter in section2:
    for i in range(1,10):
        if letter in num_to_letter[i]:
            numerical_s2.append(str(i))
            break

for letter in section3:
    for i in range(1,10):
        if letter in num_to_letter[i]:
            numerical_s3.append(str(i))
            break
number=''.join(list(letter for letter in section1) +['-']+ list((el for el in numerical_s2)) +['-']+ list((element for element in numerical_s3)))
print(number)
dictionary=dict()
print("Please enter 1 string per line, and then press enter. Write quit when you want to stop entering strings")
pangram=""
while pangram.lower()!="quit":
    pangram=input()
    dictionary[pangram]=None

letters=[]
for i in range(65,92):
    letters.append(chr(i))
for key in dictionary.keys():
    for letter in letters:
        if letter not in list(key):
            dictionary[key]="False"
            break
    if not dictionary[key]:
        continue
    dictionary[key]="True"


for key,value in zip(dictionary):
    print(f" {key}: {value}")
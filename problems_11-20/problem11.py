import re
text=input("What is the text which you want to check ")
pattern = input("What is the regex pattern")
print(re.search(pattern,text))
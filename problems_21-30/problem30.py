from re import match
year=int(input("Input a year in the format ####"))
if match("^\d{4}$",year):
    year=list(map(int,str(year)))
    print(sum(year))
else:
    print("Invalid format")
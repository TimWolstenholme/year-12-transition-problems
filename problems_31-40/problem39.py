num=0
arr=[]
while num!=-1:
    num=int(input("What is the number being added to the array, enter -1 to quit "))
odd_arr=[e for e in arr if e%2 !=0].sort()
even_arr=[element for element in arr if element not in odd_arr].sort()
print(odd_arr+even_arr)
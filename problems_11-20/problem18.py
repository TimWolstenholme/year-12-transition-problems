start=int(input("What is the start of the range"))
end=int(input("What is the end of the range"))
count=0
for i in range(start,end+1):
    year=list(str(i))
    arr=[]
    for digit in year:
        if digit in arr:
            count+=1
            continue
        else:
            arr.append(digit)
print(count)
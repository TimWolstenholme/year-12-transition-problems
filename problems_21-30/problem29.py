
def unique_items(l1:list,l2:list):
    return list(set(l2)+set(l1))
list1=[]
while True:
    item=input("Add item to list1, write -1 to quit")
    if item=='-1':
        break
    else:
        list1.append(item)
list2=[]
while True:
    item=input("Add item to list2, write -1 to quit")
    if item=='-1':
        break
    else:
        list2.append(item)

print(unique_items(list1,list2))

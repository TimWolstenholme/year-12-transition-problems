


columns=int(input("How many inputs are there: "))
headings=list(chr(n+65) for n in range(columns))
def truthtable (columns) : 
  if columns < 1:
    yield []
    return
  subtable = truthtable(columns-1)
  for row in subtable:
    for v in [0,1]:
      yield row + [v]
table= list(truthtable(columns))
print(" ",end="")
print(*(e +' 'for e  in headings))
for row in table:
    print(row)

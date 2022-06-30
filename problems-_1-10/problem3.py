def permutations(s):        
    if(len(s)==1): return [s]
    result=[]
    for i,e in enumerate(s):
        result += [e+p for p in permutations(s[:i]+s[i+1:])]
    return result
code=int(input("what is the 4 digit code: "))
perms=permutations(str(code))
for code in perms:
    print(code)
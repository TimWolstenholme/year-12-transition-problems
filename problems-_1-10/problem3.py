def permutations(code):        
    if(len(code)==1): return [code]
    result=[]
    for i,num in enumerate(code):
        result += [num+digit for digit in permutations(code[:i]+code[i+1:])]
    return result
code=(input("what is the 4 digit code: "))
perms=permutations(code)
for code in perms:
    print(code)
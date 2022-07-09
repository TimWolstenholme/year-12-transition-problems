#Caesar cipher
apply_shift=lambda letter,shift: chr(ord(letter)+shift) if not  (ord(letter)+shift<91 and letter.upper()==letter) and (ord(letter)+shift<123 and letter.lower()==letter) else chr(ord(letter)+shift-26) if not letter.isalpha() else letter
shift=int(input("What is the shift of the caesar cipher "))
while shift>26 or shift<1:
    print("Shift must be in the range 0<shift<27")
    shift=int(input("What is the shift of the caesar cipher "))
string=input("What is the string that you are applying the cipher to ")
string=list(string)
string=[apply_shift(letter,shift) for letter in string ]
string=''.join(letter for letter in string)
print(string)
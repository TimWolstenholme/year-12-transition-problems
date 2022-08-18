eng_to_morse = { 'A':'.- ', 'B':'-... ',
                    'C':'-.-. ', 'D':'-.. ', 'E':'. ',
                    'F':'..-. ', 'G':'--. ', 'H':'.... ',
                    'I':'.. ', 'J':'.--- ', 'K':'-.- ',
                    'L':'.-.. ', 'M':'-- ', 'N':'-. ',
                    'O':'--- ', 'P':'.--. ', 'Q':'--.- ',
                    'R':'.-. ', 'S':'... ', 'T':'- ',
                    'U':'..- ', 'V':'...- ', 'W':'.-- ',
                    'X':'-..- ', 'Y':'-.-- ', 'Z':'--.. '}
string=input("What is the phrase being translated: ")
string=list(string.split(' '))
phrase=[]
for word in string:
    morse_word=""
    for letter in word:
        letter=letter.upper()
        morse_word+=eng_to_morse[letter]
    phrase.append(morse_word)

phrase=''.join(word+ "| " for word in phrase)
print(phrase)


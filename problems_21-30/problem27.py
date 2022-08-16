import numpy as np
word1=input("What is the first word")
word2=input("What is the second word")
word1=list(ord(letter) for letter in word1)
word2=list(ord(letter) for letter in word2)
print(np.sum(word1)-np.sum(word2))
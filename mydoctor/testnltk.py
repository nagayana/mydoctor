import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
a="this word may not work but ? why ?"
print(len(word_tokenize(a)))
f=open("test.txt",'r')
s=""
for i in  f:
    s+=i
stok=sent_tokenize(s)
#print(stok)
cou=0
w=0
for i in stok:
    #print(i)
    cou=0
    c={}
    for item in i.split(' '):
        cou=cou+1
        if item in c:
            c[item] += 1
        else:
          c[item] =1
        
    print(c)

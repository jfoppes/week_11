#!/usr/bin/env python3

# Foppes, Jacob 
# CINF 308 Progrmaing for Informatics week 11 -  case study ch 13


# For each section of the project i will create a seperate branch with the name of the section  

import string
import random
from bisect import bisect


leFile = open("yellow_wallpaper.txt", "r") #open yellow wallpaper
leFile = leFile.read().lower() #read each line and append to list 
leFile = leFile.translate(str.maketrans('','',string.punctuation))

leString = ""
x = 0
for line in leFile: # for wach line i nthe file starting at character 730 add it to the string
    x += 1
    if x <730:
        pass
    else:
        leString = leString + line


words=(leString.split()) # create list out of all words
#print("there are",len(words),"words in Yellow wallpaper")

goodWordList = ["the","with","but","shal","will","love","that","i"]
didntMakeCut = sorted(list(set(words) - set(goodWordList)))# subtract wors in the good lsit from all words and strop in new list of not good words 

#print("these words are no inthe list ;\n",didntMakeCut)

    

#################
# 13.7

freq = {}

for i in words: # craete frequency count of words in string
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
freq = dict(sorted(freq.items(), key=lambda item: item[1]).__reversed__())

thewords = []
thecounts = []
cumulative = 0
for word,count in freq.items(): # for reach word in the freqency dict, add the count value to the cummutaive count , and add the word to words mlists, andn the count to the counts list 
    cumulative += count
    thewords.append(word)
    thecounts.append(count)

randx = random.randint(0,cumulative-1)
index = bisect(thecounts,randx)
    
    
    



######################
# 13.8
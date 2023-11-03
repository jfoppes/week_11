#!/usr/bin/env python3

# Foppes, Jacob 
# CINF 308 Progrmaing for Informatics week 11 -  case study ch 13


# For each section of the project i will create a seperate branch with the name of the section  

import string
import operator


leFile = open("yellow_wallpaper.txt", "r") #open yellow wallpaper
leFile = leFile.read().lower() #read each line and append to list 
leFile = leFile.translate(str.maketrans('','',string.punctuation))

leString = ""
x = 0
for line in leFile:
    x += 1
    if x <730:
        pass
    else:
        leString = leString + line


words=(leString.split())
#print("there are",len(words),"words in Yellow wallpaper")


freq = {}

for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
freq = dict(sorted(freq.items(), key=lambda item: item[1]).__reversed__())

common20 = []
count = 0
for i in freq.items():
    count += 1
    if count <21:
        common20.append(i)
    else: break
print("the 20 most common words are as follows;\n",common20)

    


#!/usr/bin/env python3

# Foppes, Jacob 
# CINF 308 Progrmaing for Informatics week 11 -  case study ch 13


# For each section of the project i will create a seperate branch with the name of the section  

import string
import sys


leFile = open("yellow_wallpaper.txt", "r") #open yellow wallpaper
leFile = leFile.read().lower() #read each line and append to list 
leFile = leFile.translate(str.maketrans('','',string.punctuation))

leString = ""
x = 0
for line in leFile: # for weach letter i nthe file add it to the string starting after the header that ends at latter 730
    x += 1
    if x <730:
        pass
    else:
        leString = leString + line


words=(leString.split())# make a list of all words in book 
#print("there are",len(words),"words in Yellow wallpaper")


freq = {}

for i in words: # for each word in the words lsit make a dictionary entry if one deosnt exit, increment the value for the word 
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
        
        
print(freq)


    


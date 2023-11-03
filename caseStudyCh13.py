#!/usr/bin/env python3

# Foppes, Jacob 
# CINF 308 Progrmaing for Informatics week 11 -  case study ch 13


# For each section of the project i will create a seperate branch with the name of the section  

import string
import sys

leString = open("demoText.txt", "r")
leString = leString.read().lower()

leString = leString.translate(str.maketrans('','',string.punctuation))
print(leString)

words = []
words.append(leString.split())
print(words)
    
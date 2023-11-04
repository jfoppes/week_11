#!/usr/bin/env python3

# Foppes, Jacob 
# CINF 308 Progrmaing for Informatics week 11 -  case study ch 13


# For each section of the project i will create a seperate branch with the name of the section  
import random


def histogram(s):# histogram fucntion frm section 11
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def choose_from_hist(hist): # takes a histogram'ed string and returns a reandom letter 
    keys = list(hist.keys())
    values = list(hist.values())
    choice = random.choices(keys,weights=values) # the probalbilty of returning a specific letter is based on how often it occurs in the string
    return choice
theword = 'brontosaurus'
hist = histogram(theword)
result  = choose_from_hist(hist)
print(result[0], "has a probability of",hist[result[0]]/len(theword))

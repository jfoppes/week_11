#!/usr/bin/env python3

# Foppes, Jacob 
# CINF 308 Progrmaing for Informatics week 11 -  case study ch 13


# For each section of the project i will create a seperate branch with the name of the section  

import string
import sys


leFile = open("yellow_wallpaper.txt", "r") #open yellow wallpaper
leFile = leFile.readlines() #read each line and append to list 
leString = leFile[26:] # remove the header and start at title line
print(leString)

    


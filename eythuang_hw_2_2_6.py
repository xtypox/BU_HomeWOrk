#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:01 2021
Eva Huang
CS 521 - Spring
1/27/21
Homework Problem 6
calculate leap year in for loop and while loop
@author: ehuang
"""

# Typically, any year that is evenly divisible by 4 is a leap year, with small error that needs to be account for.
# Gregorian calendar stipulates that a year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by 400.
# so 1900,2100,2100...ect are not leap years
print ("1) using for loop: ")
# forloop range 1900 to 2020
for for_year in range (1900, 2021):
    # leap year logic
    if ((for_year % 400 == 0) or (for_year % 4 == 0 and (for_year % 100 !=0))):
        print (for_year)

# while loop        
print("\n2) using while loop:")
# start counting from year 1900
while_year = 1900   
#count to 2020   
while while_year < 2021:
    while_year +=1
    
    #leap year logic
    if ((while_year % 400 == 0) or (while_year % 4 == 0 and (while_year % 100 !=0))):
        print(while_year)
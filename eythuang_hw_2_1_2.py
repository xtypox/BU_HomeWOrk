#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:01 2021
Eva Huang
CS 521 - Spring
1/26/21
Homework Problem 2
print input as string, interger and float
@author: ehuang
"""

# prompt input
ans = input("Your input: ")

# print input as interger, float, and string.
if isinstance(ans, int):
    print("your entry type is interger: ", int(ans))
elif isinstance(ans, float):
    print("your entry type is float: ", float(ans))
else:
    print("your entry type is string: ", str(ans))
    
# What data types can be input that will print without generating any errors?  Answer this question at the end of your code by using a docscring comment.
"""
technically str(intput) is always going to print without errors
"""


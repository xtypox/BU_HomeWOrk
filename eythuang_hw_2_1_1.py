#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:01 2021
Eva Huang
CS 521 - Spring
1/26/21
Homework Problem 1
(((#+2)*3)-6)/3.Use if statement to check input.
@author: ehuang
"""

# input convert to interger
num = int(input("Enter number: "))
# calc= initial num value
calc=num
# Calcualte (((num+2)*3)-6)/3
num=num+2
num=num*3
num=num-6
num=num/3

# use if statement to check input
if(calc == num):
    print("Woohoo, input matches the calculated value")
else:
    print("Boo, input doesn't the calculated value")
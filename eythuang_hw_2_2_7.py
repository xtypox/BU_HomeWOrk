#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:01 2021
Eva Huang
CS 521 - Spring
1/27/21
Homework Problem 7
rewrite for loop as a while loop.
@author: ehuang
"""
# input x to test if the for loop and while loop has the same results, we need value for x in order for the program to work
x=int(input("enter an interger: "))

#for loop provided
print("1) for loop result: ")
for i in range(1, x + 1):
	if x % i == 0:
		print(i)
        
# while loop I wrote
print("\n2) while loop result:")
# looks like we are programing for the divisor of x so thats what I did.
i=1
while i<=x:
    if(x % i == 0):
        print(i)
    i=i+1

    
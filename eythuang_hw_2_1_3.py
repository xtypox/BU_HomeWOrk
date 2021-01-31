#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:01 2021
Eva Huang
CS 521 - Spring
1/26/21
Homework Problem 3
print formula, and calculate it too
@author: ehuang
"""

# prompt input and convert to interger
ans_int = int(input("enter an interger: "))

# calculate
result=ans_int+ans_int*ans_int+ans_int*ans_int*ans_int+ans_int*ans_int*ans_int*ans_int

# print formula and result
print(ans_int,"+",ans_int,"*",ans_int,"+",ans_int,"*",ans_int,"*",ans_int,"+",ans_int,"*",ans_int,"*",ans_int,"*",ans_int,"= ",result)

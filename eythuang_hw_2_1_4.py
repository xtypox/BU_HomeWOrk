#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:01 2021
Eva Huang
CS 521 - Spring
1/26/21
Homework Problem 4
Write a three-line program that (1) prompts for a number, (2) converts the input to an integer and (3) prints the number 0 if the user input is even and the number 1 if the user input is odd
@author: ehuang
"""
# (1) prompts for a number
ans=input("enter a number: ")
# (2) converts the input to an integer
ans_int=int(ans)
# (3) prints the number 0 if the user input is even and the number 1 if the user input is odd
print(ans_int%2)
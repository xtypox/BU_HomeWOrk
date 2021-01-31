#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:47:01 2021
Eva Huang
CS 521 - Spring
1/26/21
Homework Problem 5
create BML calculator
@author: ehuang
"""
print("Let me calculater your BMI! ")
# Imperial or Metrics, y for Imperial, n for metrics. Render input to lower case
imp_or_mtr= input("Imperial units? y/n: ").lower()

# imperial 
if imp_or_mtr == "y":
    #prompt 2 input in one line
    inch, lbs = input("Please first enter the number of your height in inches then weight in lbs, separate the two numbers with a comma: ").split(",")
    #convert input to float, inch to cm
    fl_cm = float(inch)*2.45
    #convert input to float, lb to kg
    fl_kg = float(lbs)* 0.453592
    # calculation
    BMI_imp = fl_cm/(fl_kg**2)
    print("your BMI is: (",inch,"in = ", fl_cm, "cm) / (", lbs,"lb = ", fl_kg, "kg)^2 = ", BMI_imp)
    
# metric    
elif imp_or_mtr == "n":
    cm, kg = input("Please enter the number of your height in cm first then weight in kg, separated the two numbers with a comma: ").split(",")
    #convert input to float
    fl_cm = float(cm)
    #convert input to float
    fl_kg = float(kg)
    # calculation
    BMI_met = fl_cm/(fl_kg**2)
    print("your BMI is: ",cm,"cm /",kg,"kg^2 = ", BMI_met)
    
# user entered something other than Y,y,N,n 
else:
    print("oops, invalid entry")

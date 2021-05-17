#!/usr/bin/env python3

#Script: Ops Challenge 10
#Author: Ray Caoagdan
#Date of Last Revision: 05/17/2021
#Purpose: Python Conditional Statement 

##############################################################################
# Varibles list 
##############################################################################
a=input('Please input a number for a:')
b=input('Please input a number for b:')
how=("HOW DID YOU GET HERE?!?!?!?!")

##############################################################################
# Function to check if numbers are numeric value
##############################################################################
def check_variable_number():
    if a.isnumeric() and b.isnumeric(): 
        check_variables_are_equal()
    else:
        print('Error: Incorrect input detected, exititing now.')

##############################################################################
# Function to check if numbers are equal, less than, greater than
##############################################################################
def check_variables_are_equal():
    if a <= b: 
        print("a might be greater than b lets double check")
        double_check()
    elif a >=b:
        print ("a might be less than b lets double check")
        double_check()
    else:
        print (how)

##############################################################################
# Function to check if numbers are equal
##############################################################################
def double_check():
    if a == b:
        print ('Numbers are equal')
    elif a != b:
        print ('Numbers are not equal')
        print ("Lets check which one is greater")
        greater_less()
    else:
        print (how)

##############################################################################
# Function to check which number is greater
##############################################################################
def greater_less():
    if a < b:
        print ('a is less than b')
    elif a > b:
        print ('a is greater than b')
    else:
        print (how)




##############################################################################
# Main
##############################################################################
check_variable_number()
##############################################################################
# End
##############################################################################
#!/usr/bin/env python3

#Script: Ops Challenge 10
#Author: Ray Caoagdan
#Date of Last Revision: 05/17/2021
#Purpose: Python Conditional Statement 

##############################################################################
# Varibles list 
##############################################################################
a=input('Please input a number for A:')
b=input('Please input a number for B:')
how=("HOW DID YOU GET HERE?!?!?!?!")

##############################################################################
# Function to check if numbers are numeric value
##############################################################################
def check_variable_number():
    if a.isnumeric() and b.isnumeric(): 
        fist_check()
    else:
        print('Error: Incorrect input detected, exititing now.')

##############################################################################
# Function to check if numbers are equal, less than, greater than
##############################################################################
def fist_check():
    if a <= b: 
        print("A might be less than B, but lets double check")
        check_variables_are_equal()
    elif a >=b:
        print ("A might be greater than B, but lets double check")
        check_variables_are_equal()
    else:
        print (how)

##############################################################################
# Function to check if numbers are equal
##############################################################################
def check_variables_are_equal():
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
        print ('A is less than B')
    elif a > b:
        print ('A is greater than B')
    else:
        print (how)

##############################################################################
# Main
##############################################################################
check_variable_number()
##############################################################################
# End
##############################################################################
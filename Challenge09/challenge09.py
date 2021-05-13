#!/usr/bin/env python3

#Script: Ops Challenge 09
#Author: Ray Caoagdan
#Date of Last Revision: 05/12/2021
#Purpose: Python Collections

##############################################################################
# Varibles list 
##############################################################################
varlist = ["Motherboard", "CPU", "RAM", "Memory", "Cooler", "Fans", "GPU", "PSU", "Case", "RGB"]

##############################################################################
# print elements of list
##############################################################################
print(varlist[3]) #prints fourth element in list
print(" ")
print(varlist[5:10]) #prints 6-10
print(" ")
##############################################################################
# modify item in list
##############################################################################
varlist[6] = 'onion'
print(varlist)
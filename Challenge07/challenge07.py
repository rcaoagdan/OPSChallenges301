#!/usr/bin/env python3

#Script: Ops Challenge 07
#Author: Ray Caoagdan
#Date of Last Revision: 05/05/2021
#Purpose: Directory Creation - Function use

##############################################################################
# Import OS Library 
##############################################################################
import os

##############################################################################
# variables
##############################################################################
dir_input=input("Please input a directory? ")

##############################################################################
# Functions
##############################################################################

for (root, dirs, files) in os.walk(dir_input, topdown=True):
    
    print ("the root is", root)
    print ("sub directory", dirs)
    print ("the file(s)", files)



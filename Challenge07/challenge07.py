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
def dir_function(dir_input):
        for (root, dirs, files) in os.walk(dir_input, topdown=True):
                for name in files:
                        print(os.path.join(root, name))
                for name in dirs:
                        print(os.path.join(root, name))
##############################################################################
# Main
##############################################################################
dir_function(dir_input)
#!/usr/bin/env python3

#Script: Ops Challenge 06
#Author: Ray Caoagdan
#Date of Last Revision: 05/03/2021
#Purpose: Bash in Python 

##############################################################################
# Import OS Library 
##############################################################################
import subprocess

##############################################################################
# os commands stored into variables
##############################################################################
myexistence=subprocess.getoutput(["whoami"])
netinfo=subprocess.getoutput(["ip a"])
hardware=subprocess.getoutput(["lshw -short"])

##############################################################################
#Main
##############################################################################
identify_yourself= input("hello who are you? ")
print ("welcome", identify_yourself , '\n')
print ("The current user is: \n", myexistence , '\n')
print ("Displaying Network info: \n" , netinfo , '\n')
print ("The Current Hardware installed: \n", hardware , '\n')
##############################################################################
#End
##############################################################################

##############################################################################
#sources
##############################################################################
# https://www.python.org/dev/peps/pep-0008/ 
# https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
# https://docs.python.org/3/library/subprocess.html#module-subprocess 
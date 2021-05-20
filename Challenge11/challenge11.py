#!/usr/bin/env python3

#Script: Ops Challenge 11
#Author: Ray Caoagdan
#Date of Last Revision: 05/19/2021
#Purpose: Python File Handling

import os
##############################################################################
# Create new file 
##############################################################################
testfile = open("newtext.txt" , "w")

##############################################################################
# Append the file
##############################################################################
testfile.write("Hello, World \n")
array = ["Number 1 \n", "Number 2 \n","Nubmer 3 \n"]
testfile.writelines(array)
testfile.close()#closes file  to change file access

##############################################################################
# Open files and reads
##############################################################################
testfile = open("newtext.txt", "r+")
print( )
print("The very first line is \n")
print (testfile.readline( ))
testfile.close() 

##############################################################################
# Delete file
##############################################################################
print( )
print("Shall we delete the file?")
response=input('Y-Yes | N-No: ')
  
   

def delete_confirm():
    if response == "Y" or response == "y" or response =="YES" or response =="yes" or response =="Yes" or response =="YEs" or response =="YeS" or response =="yES":
        print("Deleting file now \n")
        os.remove("newtext.txt")
        print("File Deleted")
    elif response == "N" or response == "n" or response == "no" or response == "No" or response == "NO" or response == "nO":
        print("The file shall stay")
    else:
        print("Incorrect selection")
       


##############################################################################
# Main
##############################################################################
delete_confirm()
##############################################################################
# End
##############################################################################
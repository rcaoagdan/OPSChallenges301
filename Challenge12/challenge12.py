#!/usr/bin/env python3

#Script: Ops Challenge 12
#Author: Ray Caoagdan
#Date of Last Revision: 05/24/2021
#Purpose: Python Psutil

##############################################################################
# import psutil
##############################################################################
import psutil 


##############################################################################
#Main
##############################################################################
print('Hello Welcome! \n')
print('user: Time Spent in User mode')
print('nice: Time Spent in User mode low priority')
print('sytem: Time Spent in System Mode')
print('idle: Time Spent in idle tasks')
print('iowait: Time Spent waiting for I/O to comeplte')
print('irq: Time Spent Hardware interrupts')
print('softirq: To Spent Software Interrupts')
print('steal: Time spent bu other O/S running in a virtuialized enviorment ')
print('guest_nice: Time Spent running a virtual CPU for guest OS under control of Linux Kernel \n')

##############################################################################
#Saves information to text file
##############################################################################
testfile = open("newfile.txt", "w")
psinfo=psutil.cpu_times()
strpsinfo=str(psinfo) #converts float value to string
testfile.writelines(strpsinfo)
testfile.close()

##############################################################################
#Print information from text file
##############################################################################
testfile = open("newfile.txt", "r+")
print()
print(testfile.readline())
testfile.close

##############################################################################
#End
##############################################################################


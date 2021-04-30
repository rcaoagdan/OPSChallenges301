#!/bin/sh

#Script: Ops Challenge 05
#Author: Ray Caoagdan
#Date of Last Revision: 04/26/2021
#Purpose: Clearing Logs - RUN with sudo bash

##############################################################################
# syslog log and event information for linux 
# print contents
# clear contents and print out 

##############################################################################
syslog_function(){
    echo "The currents contents of System Logs:"
    echo " "
    cat /var/log/syslog
    echo -e "\nClearing  logs now"
    echo " "
    >/var/log/syslog
    echo " "
    cat /var/log/syslog
}
##############################################################################
# WTMP keeps historyt of all logins and logouts
# print contents log file 
# clear contents and print out contnets
##############################################################################
wtmp_function (){
    echo -e "\nCurrents contents of WTMP:"
    echo " "
    cat /var/log/wtmp
    echo -e "\nClearing  WTMP logs now"
    echo " "
    >/var/log/wtmp
    cat /var/log/wtmp
}
##############################################################################
# main 
##############################################################################
syslog_function

wtmp_function
##############################################################################
# End
##############################################################################
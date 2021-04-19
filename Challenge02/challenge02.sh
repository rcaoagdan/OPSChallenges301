#!/bin/sh
#
#Script: Ops Challenge 02 
#Author: Ray Caoagdan
#Date of Last Revision: 04/18/2021
#Purpose: Arrays : Append; Date&Time 

##############################################################################
# Variabeles used 
# https://www.lifewire.com/display-date-time-using-linux-command-line-4032698 
# site above resource for displaying current date and time
##############################################################################
date_time=$(date +%d/%m/%Y-%H:%M:%S)

##############################################################################
# copy files fuction:
# scp = securely copies 
# when copying files scp /file_path  /Destination_path 
# a . can be used to refer to current directory
##############################################################################
copy_files(){
    scp /var/log/syslog .   
}

##############################################################################
# appends newly created file with current date and time
##############################################################################
append_file(){
    copy_files
    echo "Current: $date_time" >> syslog
}


#main
echo "Hello! it is currently $date_time"
echo ""
echo "============================ Copying System Log Files ====================================="
echo ""
echo "[========                                                                                  ]"
echo "[==============================                                                            ]"
echo "[=======================================================                                   ]"
echo "[==================================================================================        ]"
echo "[==========================================================================================]"
echo ""
echo "=====================  Systems Log Files Copied to current directory  ====================="
append_file
#end
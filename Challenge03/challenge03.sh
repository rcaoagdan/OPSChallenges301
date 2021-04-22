#!/bin/sh
#
#Script: Ops Challenge 03
#Author: Ray Caoagdan
#Date of Last Revision: 04/20/2021
#Purpose: File Permission

##############################################################################
# Variabeles used 
# $dirpath User input Directory Path
# $per User input Permission
##############################################################################
echo "Hello enter a directory path:"
read -r dirpath
echo "Enter Permission Number:"
read -r per 

##############################################################################
# Fuction use to check if Directory input is correct
# If path exists then it runs Permision Function
# If path does not exsits, then user will be prompted 
##############################################################################
dir_path_exists(){
    if [ -f "$dirpath" ]; then
    ls -l "$dirpath"
    else
    echo "ERROR: Directory does not exists"
    fi
}


##############################################################################
# Main Function
# If both path exisits and permision input is a number 
# Function will run chmod 
##############################################################################
change_files_settings(){
    dir_path_exists
    chmod "$per" "$dirpath"
}
change_files_settings
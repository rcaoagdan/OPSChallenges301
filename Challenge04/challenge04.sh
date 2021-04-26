#!/bin/sh

#Script: Ops Challenge 04
#Author: Ray Caoagdan
#Date of Last Revision: 04/25/2021
#Purpose: Conditional Menu System


##############################################################################
# Function used to print out greatest saying in the world
##############################################################################
greatest_saying_ever(){
    echo " "
    echo "Hello World!"
    main_menu
}
##############################################################################
# Function used to ping computers loopback address
##############################################################################
ping_myself(){
    echo " "
    ping -c 4 localhost
    main_menu
}
##############################################################################
# Function used to print out IP Info
##############################################################################
ip_info(){
    echo " "
    echo "Printing IP Info"
    ifconfig
    main_menu
}

##############################################################################
# Function used to "exit"
##############################################################################
fake_exit(){
    echo " "
    echo "Welcome To Hotel California!!"
    main_menu
}
##############################################################################
# Function used secretly exit
##############################################################################
real_exit(){
    echo " "
    echo "There is no place like home!"
    echo "Have a nice day!"
    exit
}
##############################################################################
# Function 404 error
##############################################################################
error_glitch(){
    echo " "
    echo "ERROR ERROR ERROR"
    echo "ERROR ERROR ERROR"
    echo "Glitch in the matrix"
    echo "Exiting for safety"
    exit
}
##############################################################################
# Main 
##############################################################################
main_menu(){
    echo -e "\nHello, Please select what you want to do"
    echo -e "1. Print the greatest saying in the world"
    echo -e "2. Ping yourself"
    echo -e "3. Print IP information"
    echo -e "4. Exit"
    read -r mainsel

    while :
    do 
        if [ "$mainsel" == 1 ] ; then
           greatest_saying_ever
        elif [ "$mainsel" == 2 ] ; then
           ping_myself
        elif [ "$mainsel" == 3 ] ; then
            ip_info
        elif [ "$mainsel" == 4 ] ; then
            fake_exit
        elif [ "$mainsel" == "127.0.0.1" ] ; then
            real_exit
        elif [ "$mainsel" == 404 ] ; then
            error_glitch
        else 
            echo -e  "\n Please make a correct option" 
            main_menu
        fi
    done
}

main_menu
##############################################################################
# End
##############################################################################
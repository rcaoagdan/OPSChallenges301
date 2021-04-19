#!/bin/sh

#Script: Ops Challenge 02 
#Author: Ray Caoagdan
#Date of Last Revision: 04/18/2021
#Purpose: Arrays : Append; Date&Time 

#variables
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)
hour=$(date +%H)
minute=$(date +%M)
second=$(date +%S)

#function
date_and_time(){
    echo "The Current date:" $day-$month-$year
}
date_and_time
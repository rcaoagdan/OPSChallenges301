#!/usr/bin/env python3

#Script: Ops Challenge 13
#Author: Ray Caoagdan
#Date of Last Revision: 05/25/2021
#Purpose: HTTP GET request with Python

##############################################################################
# import request into Python Script 
##############################################################################
import requests 

##############################################################################
# Prompts User to enter a URL 
##############################################################################
print('Hello, Welcome to HTTP reqeust information')
print('Please enter a URL')
print('Ensure its in this following format: http://website or https://website')
website_url = input( )

##############################################################################
# Asks user what request they wish to see 
##############################################################################
print( )
print('What request would you like to see? \n')
print('1.GET')
print('2.POST')
print('3.PUT')
print('4.DELETE')
print('5.HEAD')
print('6.PATCH')
print('7.OPTION')
response = input('Desired Request:')

##############################################################################
# Main Fuction 
# Checks user input of desired request 
# Calls fuction of the request
##############################################################################
def request_response():
    if response == '1':
        get_request()
    elif response == '2':
        post_request()
    elif response == '3':
        put_request
    elif response == '4':
        delete_request
    elif response == '5':
        head_request
    elif response == '6':
        patch_request
    elif response == '7':
        options_request
    else:
        print('ERROR: Incorrect selection made')

##############################################################################
# Get Request  
##############################################################################
def get_request():
    getrequest = requests.get(website_url)
    if getrequest.status_code == 200:
        print('Success \n')
    elif getrequest.status_code == 301:
        print('Site Moved Permanently \n')
    elif getrequest.status_code == 404:
        print('Not Found \n')
    else:
        print('Status code: \n')
        print(getrequest.status_code)
    
##############################################################################
# Post Request  
##############################################################################
def post_request():
    postrequest = requests.post(website_url)
    print(postrequest.status_code)
    

##############################################################################
# Put Request  
##############################################################################
def put_request():
    putrequest = requests.put(website_url)
    print(putrequest.status_code)

##############################################################################
# Delete Request  
##############################################################################
def delete_request():
    deleterequest = requests.delete(website_url)
    print(deleterequest.status_code)

##############################################################################
# Head Request  
##############################################################################
def head_request():
    headrequest = requests.head(website_url)
    print(headrequest.status_code)

##############################################################################
# Patch Request  
##############################################################################
def patch_request():
    patchrequest = requests.patch(website_url)
    print(patchrequest.status_code)

##############################################################################
# Options Request  
##############################################################################
def options_request():
    optrequest = requests.options(website_url)
    print(optrequest.status_code)

##############################################################################
# Main 
##############################################################################
request_response()

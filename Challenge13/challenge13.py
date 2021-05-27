#!/usr/bin/env python3

#Script: Ops Challenge 13
#Author: Ray Caoagdan
#Date of Last Revision: 05/25/2021
#Purpose: HTTP GET request with Python

##############################################################################
# import request into Python Script 
##############################################################################
import requests
from requests.api import post 

##############################################################################
# Variables
# HTTP status msgs
##############################################################################
code200 = ("Success \n")
code202 = ("Accepted \n")
code204 = ("No Content \n")
code301 = ("Site Moved Permanently \n")
code403 = ("ERROR:Forbidden \n")
code404 = ("ERROR:NOT FOUND \n")
code405 = ("ERROR:Method Not Allowed \n")
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
        put_request()
    elif response == '4':
        delete_request()
    elif response == '5':
        head_request()
    elif response == '6':
        patch_request()
    elif response == '7':
        options_request()
    else:
        print('ERROR: Incorrect selection made')

##############################################################################
# Get Request  
##############################################################################
def get_request():
    print( )
    getrequest = requests.get(website_url)
    print(getrequest.url)
    if getrequest.status_code == 200:
        print(code200)
    elif getrequest.status_code == 301:
        print(code301)
    elif getrequest.status_code == 404:
        print(code404)
    else:
        print('Status Not Known')
        
    
##############################################################################
# Post Request  
##############################################################################
def post_request():
    postrequest = requests.post(website_url)
    print(postrequest.url)
    if postrequest.status_code == 200:
        print(code200)
    elif postrequest.status_code == 403:
        print(code403)
    elif postrequest.status_code == 405:
        print(code405)
    else:
        print('Status Unknown')
    

##############################################################################
# Put Request  
##############################################################################
def put_request():
    putrequest = requests.put(website_url)
    print(putrequest.url)
    print(putrequest.status_code)
    if putrequest.status_code == 200:
        print(code200)
    elif putrequest.status_code == 405:
        print(code405)
    else:
        print('Status Unknown')

##############################################################################
# Delete Request  
##############################################################################
def delete_request():
    print( )
    print('request:DELETE ')
    deleterequest = requests.delete(website_url)
    print(deleterequest.url)
    if deleterequest.status_code == 200:
        print(code200)
    elif deleterequest.status_code == 202:
        print(code202)
    elif deleterequest.status_code == 204:
        print(code204)
    elif deleterequest.status_code == 405:
        print(code405, '\n')
    else:
        print('status unknown')


##############################################################################
# Head Request  
##############################################################################
def head_request():
    print( )
    headrequest = requests.head(website_url)
    print(headrequest.url)
    if headrequest.status_code == 200:
        print(code200)
    elif headrequest.status_code == 301:
        print(code301)
    elif headrequest.status_code > 400 and headrequest < 500:
        print('ERROR')
    else:
        print('Status Unknown')


##############################################################################
# Patch Request  
##############################################################################
def patch_request():
    print()
    patchrequest = requests.patch(website_url)
    print(patchrequest.url)
    if patchrequest.status_code == 200:
        print(code200)
    elif patchrequest.status_code == 403:
        print(code403)
    elif patchrequest.status_code == 405:
        print(code405)
    else:
        print ('Status Unknown')

##############################################################################
# Options Request  
##############################################################################
def options_request():
    print()
    optrequest = requests.options(website_url)
    print(optrequest.url)
    if optrequest.status_code == 200:
        print(code200)
    elif optrequest.status_code == 403:
        print(code403)
    elif optrequest.status_code == 405:
        print(code405)
    else:
        print ('Status Unknown')

##############################################################################
# Main 
##############################################################################
request_response()
##############################################################################
# End
##############################################################################
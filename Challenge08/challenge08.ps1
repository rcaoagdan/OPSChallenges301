# Script : Ops Challenge 08
# Author : Ray Caoagdan
# Date of Last Revision : 05/10/2021
# Purpose : Powershell add new user to AD
##############################################################################
# Variables
##############################################################################
$firstname = Read-Host -Prompt 'Enter User First Name'
$lastname = Read-Host -Prompt 'Enter User Last Name'
$fullname = "$firstname $lastname"
$jobtitle = Read-Host -Prompt 'Enter Users Job Title'
$newuser = Read-Host -Prompt 'Enter Username'
$passwrd = Read-Host 'Enter Password' -AsSecureString

##############################################################################
# Add User
##############################################################################
function addUSER {
	New-ADUser -Name $fullname -GivenName $firstname -Surname $lastname -SamAccountName $newuser -AccountPassword $passwrd  -Enabled $True
	
}
##############################################################################
# Confirm Information
##############################################################################
function confirmInfo {
	Write-Output " "
	Write-Output "Hello Please Confirm the information is correct "
	Write-Output "First name: $firstname"
	Write-Output "Last name: $lastname"
	Write-Output "Job Title: $jobtitle"
	Write-Output "Username: $newuser"
	Write-Output "Pasword: $passwrd"
	$confriminfo = Read-Host "1. Info is correct | 2. Info is not correct"
	if($confriminfo -eq 1){
    	addUSER
	}
	elseif($confriminfo -eq 2){
    	Write-Output "Not Adding user"
	}
	else{
    	Write-Output "Please Make a correct selection"
    	confirmInfo
	}
}
#main
confirmInfo
#end


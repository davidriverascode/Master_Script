#!/usr/bin/env python3
#pveum useradd name@realm -comment "Comment"
#pvesh set /access/password --userid "testuser@realm" --password "least_five_chars"
import subprocess

print("DeLeTe new users script")
rootname = input("Enter root of username (e.g. student will become studentn): ")
startusers = input("Enter starting number for users in digits: ")
numusers = input("Enter number of users in digits: ")
#comment = raw_input("Enter user comment e.g. 'Standard student user': ")
#fullsteamahead = False
areyousure = input("YOU ARE ABOUT TO DELETE USERS! ARE YOU SURE? If Yes, enter FrObScOtTlE: ")
if areyousure == "FrObScOtTlE":
	for i in range(int(startusers), (int(numusers)+int(startusers))):
        	usernm = rootname + str(i)
        	args = "pveum userdel " + usernm + "@pve" 
        	print("********")
        	print(args)
        	print("********")
        	subprocess.call(args, shell=True)
else:
	print("Aborted!")

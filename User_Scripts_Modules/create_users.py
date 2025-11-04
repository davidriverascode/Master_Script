#!/usr/bin/env python3
#pveum useradd name@realm -comment "Comment"
#pvesh set /access/password --userid "testuser@realm" --password "least_five_chars"
import subprocess
import time

def run():

	print ("Create new users script")
	rootname = input("Enter root of username (e.g. student will become studentn): ")
	startusers = input("Enter starting number for users in digits: ")
	numusers = input("Enter number of users in digits: ")
	comment = input("Enter user comment e.g. 'Standard student user': ")
	days_to_expire = float(input("Enter days until account should expire (0 for never): "))

	# Calculate time since epoch in seconds from the amount of days that user inputted
	expire_epoch_secs = int(int(time.time()) + (days_to_expire * 24 * 60 * 60))

	# Set epoch_secs to 0 if user inputted 0, so that the account will never expire
	if float(days_to_expire) == 0.0: expire_epoch_secs = 0

	fullsteamahead = False
	for i in range(int(startusers), (int(numusers)+int(startusers))):
		usernm = rootname + str(i)
		# args = "pveum useradd " + usernm + "@pve -comment " + '"' + comment + '"'
		args = f'pveum user add {usernm}@pve --comment "{comment}" --expire {expire_epoch_secs}'
		print ("********")
		print (args)
		print ("********")
		subprocess.call(args, shell=True)
		setdefaultpassword = "pvesh set /access/password --userid " + '"' + usernm + '@pve" --password "1*Changeme"'
		subprocess.call(setdefaultpassword, shell=True)
		print(f"\n > Time: {(int(time.time()) + (days_to_expire * 24 * 60 * 60))}")
	return "Success"

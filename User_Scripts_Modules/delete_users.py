#!/usr/bin/env python3
#pveum useradd name@realm -comment "Comment"
#pvesh set /access/password --userid "testuser@realm" --password "least_five_chars"
import subprocess


def run():

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
	        	print(args)
	        	subprocess.call(args, shell=True)
	else:
		print("Aborted!")

	return "Success"

def delete_users(rootname, users_list, pre=""):

	# Iterate through the list of users, if the rootname matches the desired rootname, delete that user
	user_count = 0
	for user in users_list:
		sections = user.split("-")
		new_user = user.replace(sections[-1], "")
		# If the rootname is found in the username
		if new_user == rootname:
			args = f"pveum userdel {user}"
			print(f"{pre}********")
			print(f"{pre}> {args}")
			print(f"{pre}********")
			subprocess.call(args, shell=True)
			user_count += 1
	if user_count == 0:
		print(f"{pre}There were no users to delete")
	else:
		print(f"{pre}Your users have been deleted")
	return "Success"

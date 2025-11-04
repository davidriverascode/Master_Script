#!/usr/bin/env python3
import subprocess

def run():

	print("How many users would you like to remove from vm(s)?")
	user_amount = input("#)")

	try:
		user_amount = int(user_amount) # Turn the string input into an integer
	except:
		print("That is not a valid number, please try again.")
		return

	if user_amount == 1: # This logic will call a function based off of how many users the user wants to remove
		remove_one_user()
	elif user_amount > 1:
		remove_several_users(user_amount)
	else:
		print("That is not a valid number, please try again.") # This will only happen if the number of users is negative
		return
	return "Success"

def remove_one_user():
	#pvum aclmod /vms/id -users username@realm -roles PVEVMUser

	print ("Batch REMOVE SINGLE user FROM VMs.")
	rootname = input("Enter username (e.g. hread-1): ")
	startvms = int(input("Enter Starting mumber for VMs in digits: "))
	totalusersvms = int(input("Enter total number of vms in digits: "))
	roles = input("Enter the role/permissions for users to REMOVE (e.g. PVEVMUser): ")
	for i in range(startvms, (startvms+totalusersvms)):
	        args = "pveum acl delete /vms/" + str(startvms) + " -users " + rootname + "@pve -roles " +roles
	        print (args)
	        subprocess.call(args,shell=True)
	        startvms += 1

	return "Success"

def remove_several_users(totalusersvms):

	#pvum aclmod /vms/id -users username@realm -roles PVEVMUser

	print ("Batch REMOVE users FROM VMs.")
	rootname = input("Enter root of username (e.g. student will become studentn): ")
	startusers = int(input("Enter starting number for users in digits: "))
	startvms = int(input("Enter Starting mumber for VMs in digits: "))
	# totalusersvms = int(input("Enter total number of users/vms in digits: "))
	roles = input("Enter the role/permissions for users to REMOVE (e.g. PVEVMUser): ")
	for i in range(startusers, (totalusersvms+startusers)):
	        args = "pveum acl delete /vms/" + str(startvms) + " -users " + rootname + str(i) + "@pve -roles " +roles
        	print (args)
        	subprocess.call(args,shell=True)
        	startvms += 1

	return "Success"

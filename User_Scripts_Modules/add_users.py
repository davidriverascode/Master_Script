#!/usr/bin/env python3
#pvum aclmod /vms/id -users username@realm -roles PVEVMUser
import subprocess


def run():
	# Ask how many users to be created
	user_amount = input("\nHow many users will you be adding?")

	try:
		user_amount = int(user_amount)
	except:
		print("That is not a number, please try again")
		return

	# Run the function based off of user answer
	if user_amount == 1:
		add_single_user()
	elif user_amount != 1 and user_amount > 1:
		add_multiple_users(user_amount)

	return "Success"

def add_single_user():

	print ("Batch add a SINGLE user to several VMs.")
	rootname = input("Enter username (e.g. hread): ")

	#startusers = int(raw_input("Enter starting number for users in digits: "))
	startvms = int(input("Enter the starting VMID of the machines that you would like to add the user to: "))
	totalusersvms = int(input("Enter total number of vms in digits: "))
	roles = input("Enter the role/permissions for user (e.g. PVEVMUser): ")
	for i in range(startvms, (totalusersvms+startvms)):
		args = "pveum aclmod /vms/" + str(startvms) + " -users " + rootname + "@pve -roles " +roles
		print (args)
		subprocess.call(args,shell=True)
		startvms += 1

	return "Success"

def add_multiple_users(totalusersvms):

	print ("Batch add users to VMs as standard users.")
	rootname = input("Enter root of username (e.g. student-): ")
	startusers = int(input("Enter starting number for users in digits: "))
	startvms = int(input("Enter Starting mumber for VMs in digits: "))
	# totalusersvms = int(input("Enter total number of users/vms in digits: "))
	roles = input("Enter the role/permissions for users (e.g. PVEVMUser): ")
	for i in range(startusers, (totalusersvms+startusers)):
        	args = "pveum aclmod /vms/" + str(startvms) + " -users " + rootname + str(i) + "@pve -roles " + roles
        	print (args)
        	subprocess.call(args,shell=True)
        	startvms += 1

	return "Success"

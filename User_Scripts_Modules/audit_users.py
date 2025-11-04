#!/usr/bin/env python3
import subprocess
import time
from . import delete_users, get_name_of_vmid, stop_vms

def get_assoc_vms(username):
	args = f'cat /etc/pve/user.cfg | grep -v "user:" | grep "{username}" > ./user_assoc_vms/{username}.txt'
	subprocess.call(args, shell=True)

	assoc_vms = open(f"./user_assoc_vms/{username}.txt", "r")

	vmid_list = []

	for vm in assoc_vms:
		sections = vm.split(":")
		vmid = sections[2].replace("/vms/", "")
		vmid_list.append(vmid)

	if not vmid_list:
		return None

	vms_dictionary = get_name_of_vmid.get_name(None, vmid_list)

	return vms_dictionary

def run():

	# Update users list
	args = 'cat /etc/pve/user.cfg | grep "user:" > users_list.txt'
	print(f" > Updating Users List . . .\n{args}")
	subprocess.call(args, shell=True)

	expired_users_list = []

	# Open the users list file
	ul_file = open("users_list.txt", "r")

	# Searches through the users list file for expired users
	for line in ul_file:
		params = line.split(":")
		expired = params[3]

		# If they are expired, add them to the list of expired users
		if int(expired) != 0 and int(expired) < time.time():
			expired_users_list.append(params[1])

	ul_file.close()

	# Show the user the expired users in a nice format
	print("\n*************************************************")
	print("\n > Expired Users Found:\n")
	print("_____________________________________________________________________")
	print("|    Users         | Virtual Machines {'VMID':'Name of VM'}")
	print("|--------------------------------------------------------------------")
	for expired_user in expired_users_list:
		print(f"|    {'{:<13}'.format(expired_user.replace('@pve', ''))} | {get_assoc_vms(expired_user)}")
	print("|____________________________________________________________________")
	print("\n*************************************************")


	# Give them the option to delete said users
	print("\nWhat would you like to do? Type a number:\n")
	print("1. DELETE ALL USERS")
	print("2. DELETE ALL USERS and all VIRTUAL MACHINES associated with them")
	print("3. DELETE A GROUP OF USERS")
	print("4. DELETE A GROUP OF USERS and all VIRTUAL MACHINES associated with them")
	print("\n**If you want do nothing, hit enter**")
	who_del = input("\n > ")

	bloody_lot = "dEl3t3 tH3 bLooDY lOt"

	# DELETE ALL USERS
	if who_del == "1":
		print("\n\n > ARE YOU SURE THAT YOU WANT TO DELETE ALL USERS???? ")
		print(" > IF NOT, PRESS ENTER")
		print(f" > IF YOU ARE, TYPE:  {bloody_lot}")
		sure = input(" > ")
		if sure == bloody_lot:
			for user in expired_users_list:
				args = f"pveum user delete {user}"
				subprocess.call(args, shell=True)
		elif sure == "":
			pass
		else:
			print("\nYou typed the incorrect phrase. Aborting")

	# DELETE ALL USERS and VMS
	elif who_del == "2":
		print("\n\n > ARE YOU ABSOLUTELY POSITIVE THAT YOU WANT TO DELETE ALL OF THESE USER AND THE VMS THAT ARE ASSOCIATED WITH THEM????")
		print(" > THIS PROCESS IS NON-REVERSIBLE")
		print(" > IF NOT, PRESS ENTER")
		print(f" > IF YOU ARE POSITIVE, THEN TYPE:  {bloody_lot}")

		sure = input("\n > ")
		if sure == bloody_lot:

			# Delete vms
			for user in expired_users_list:
				vm_dictionary = get_assoc_vms(f"{user}")
				if vm_dictionary != None:
					for vm in vm_dictionary:
						args = f"qm destroy {vm}"
						print(args)
						subprocess.call(args,shell=True)
				else:
					print("No vm to delete")
			# Delete users
			for user in expired_users_list:
				args = f"pveum user delete {user}"
				print(args)
				subprocess.call(args, shell=True)

		elif sure == "":
			pass
		else:
			print("\nYou typed the incorrect phrase. Aborting")

	# DELETE USERS BY GROUP
	elif who_del == "3":
		rootname = input("Enter the rootname of the users you would like to delete e.g. (user-): ")
		delete_users.delete_users(rootname, expired_users_list)

	# DELETE USERS BY GROUP and their VMS
	elif who_del == "4":

		rootname = input("Enter the rootname of the users you would like to delete e.g. (user-): ")

		print("_____________________________________________________________________________________")
		print("|")
		print("| ARE YOU ABSOLUTELY POSITIVE THAT YOU WANT TO DELETE ALL OF THESE USER AND THE VMS THAT ARE ASSOCIATED WITH THEM????")
		print("|")
		print("| THIS PROCESS IS NON-REVERSIBLE")
		print("| If not, press enter")
		print(f"| If you are POSITIVE, then type:  {bloody_lot}")

		print("|")
		sure = input("| > ")
		if sure == bloody_lot or sure == " ":

			# Find all of the users with that rootname
			usernames_list = []
			for user in expired_users_list:
				old_user = user
				user = user.replace("@pve", "")
				if user.count("-") > 1:
					user_list = user.split("-")
					user = "-".join(user_list[:-1]) + "-"
				elif user.count("-") == 1:
					user_list = user.split("-")
					user = user_list[0] + "-"
				elif user.count("-") == None or user.count("-") == 0:
					user = user
				else:
					return "User not found, they must not be expired, try again."

				if user == rootname:
					usernames_list.append(old_user)

			for username in usernames_list:
				# Delete assoc VMS if it has the rootname that the user entered
				vms = get_assoc_vms(f"{username}")
				if vms != None:
					print("|___________________________________________________________________________")
					print("|     User                      | Virtual Machine that is getting deleted")
					for vm in vms:
						print(f"|    {'{:<26}'.format(username)} | {vm}")
						stop_vms.stop_machine(vm)
						args = f"qm destroy {vm}"
						subprocess.call(args, shell=True)

			# Delete the users
			print("|\n| Deleting the users... ")
			delete_users.delete_users(rootname, expired_users_list, "| ")
			print("|___________________________________________________________________________")


	elif who_del == "":
		pass
	else:
		print("That was not an option. Aborting")

	return "Success"


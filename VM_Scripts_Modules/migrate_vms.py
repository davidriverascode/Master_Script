#!/usr/bin/env python3
#qm snapshot vmid snapname
import subprocess

def run():

	print("Script for MIGRATION - run when VM is off!")
	print("All numbers in digits please")

	# Gather information about the VMs
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to migrate: ")
	nodename = input("Enter NODE to migrate to (one word only): ")

	# Loop through for the amount of VMs
	for i in range(int(startvm), (int(endvm)+1)):

		# Combine everything into the command to execute
	        args = "qm migrate " + str(i) + " " + nodename

		# Show the user the command
	        print(args)

		# Execute the command in the shell
	        subprocess.call(args, shell=True)

	return "Success"

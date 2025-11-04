#!/usr/bin/env python3
#qm start vmid
import subprocess

def run():

	print("Resume (from hibernate) All numbers in digits please")

	# Gather the information about the VMs
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to start: ")

	# Loop for the amount of VMs
	for i in range(int(startvm), (int(endvm)+1)):

		# Combine everything into a command to execute
	        args = "qm resume " + str(i)

		# Show the user the command
	        print(args)

		# Execute the command in the shell
	        subprocess.call(args, shell=True)

	return "Success"

#!/usr/bin/env python3
# Example command: qm suspend vmid --todisk 1
import subprocess

def run():

	print("Script for hibernation to disk")
	print("All numbers in digits please")

	# Gather information about the VMs to hibernate
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to hibernate: ")

	# Loop for the amount of VMs
	for i in range(int(startvm), (int(endvm)+1)):

		# Combine everything into a command to execute
	        args = "qm suspend " + str(i) + " --todisk 1"

		# Show the user the command
	        print(args)

		# Execute the command
	        subprocess.call(args, shell=True)

	return "Success"

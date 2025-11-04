#!/usr/bin/env python3
# Example command: qm destroy vmid
import subprocess

def run():

	print ("WARNING! THIS WILL DESTROY VMs! All numbers in digits please")

	# Gather information about the VMs
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to destroy: ")

	# Make sure that user wants to perform this action
	really = input("Are you sure? Type FroBscOttlE if sure!")

	if really == "FroBscOttlE":
		# Loop for the amount of VMs
		for i in range(int(startvm), (int(endvm)+1)):

			# Command to execute
			args = "qm destroy " + str(i)

			# Show the command to the user
			print (args)

			# Execute the command
			subprocess.call(args, shell=True)
	else:
		print ("Aborted")
		return "Failure"

	return "Success"

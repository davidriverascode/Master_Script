#!/usr/bin/env python3
# Example command: qm snapshot vmid snapname
import subprocess

def run():

	print("Script for deleting snapshots - run when VM is off!")
	print("All numbers in digits please")

	# Gather information about the VMs and the snapshot
	startvm = input("Enter starting VM Number: ")
	endvm = input("Enter last VM to DELETE snapshot: ")
	snapname = input("Enter Snapshot name (one word only): ")

	# Loop for the amount of VMs
	for i in range(int(startvm), (int(endvm) + 1)):

		# Combine everything into the command that we want to execute
	        args = "qm delsnapshot " + str(i) + " " + snapname

		# Show the command to the user
	        print (args)

		# Execute the command in the shell
	        subprocess.call(args, shell=True)

	return "Success"

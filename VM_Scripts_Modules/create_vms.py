#!/usr/bin/env python3
#example of the command that will be run: qm clone 105 106 --name df423-1
import subprocess
from . import find_vmid_slot_module

def run():

	print("All numbers in digits please")

	# Get information on the machines to clone

	templatevm = input("VMID of your Template: ")
	totalvm = input ("Number of VMs to clone: ")
	vmname = input("How do you want to name the vm? E.g. 'df423-' n.b. number added automatically after '-': ")
	node = input("Which node do you want to create the VM on? E.g. foxtrot: ")
	description = input("Description of VM: ")

	# Uses the find vmid slot module to find a slot of VMIDs that are not currently being used
	startvm = find_vmid_slot_module.find_free_vmids(totalvm)[0]

	# Informs the user of the slot that was found
	print("Startvm: ", startvm)

	# Loop through for the amount of VMs that are to be cloned
	for i in range(0, int(totalvm)):

		currvm = int(startvm) + i
		currname = vmname+str(i+1)

		# Combine all of the information into the CLI command that we want to execute
		args = f'qm clone {templatevm} {str(currvm)} --name {currname} --full false --target {node} --description "{description}"'


		# Print out the command for the user to see
		print(args)

		# Use subprocess to execute the command in the shell
		subprocess.call(args, shell=True)

	return "Success"

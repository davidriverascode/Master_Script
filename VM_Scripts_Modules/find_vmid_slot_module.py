#!/usr/bin/env python3

import subprocess

#/etc/pve/.vmlist  <- path to vmlist

# This function gets an updated version of the vmlist and return the vmids as a sorted list
def get_vmlist():

	# This stores the .vmlist data in a text file so we can read it
	ans = subprocess.run("cat /etc/pve/.vmlist > temp.txt", shell=True)

	# Open the temporary text file
	file = open("temp.txt", "r")

	available_vmids_list = []

	# Search through vmlist text file
	for line in file:
		# Extract the VMID from the current line
		vmid_start = line.find('"')
		vmid_end = line.find('":')
		vmid = line[(vmid_start + 1):vmid_end]

		# This skips over the values that are not integers
		try:
			vmid = int(vmid)
		except:
			pass
		else:
			# Store the VMID in the list
			available_vmids_list.append(vmid)

	file.close()

	# Sort the vmlist array
	sorted_list = sorted(available_vmids_list)
	sorted_list.append(999)

	return sorted_list

# This function take an amount of vmids, and finds an open slot within a sorted list of vmids
def find_free_vmids(amount_of_vmids):
	sorted_list = get_vmlist()
	amount_of_vmids = int(amount_of_vmids)

	# Starting value
	old_vmid = 100

	# Loop through list
	for vmid in sorted_list:

		# If there is an available slot
		if (vmid - old_vmid) > (amount_of_vmids + 1):
			# Get exact starting and ending vmids
			first_vmid = old_vmid + 1
			last_vmid = first_vmid + amount_of_vmids

			print("Yay found a slot! The range is from vmid [", first_vmid, " - ", last_vmid, "]")
			return [first_vmid, last_vmid]
		else:
			# Change the last vmid to the current before loop iteration
			old_vmid = vmid

	return "There is not space for the inputted range"


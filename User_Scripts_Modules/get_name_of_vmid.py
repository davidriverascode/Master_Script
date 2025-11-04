#!/usr/bin/env python3
import subprocess
import json

def get_name(vmid, vmid_list=[]):

	# Update vms json file
	args = "pvesh get /cluster/resources --type vm --output-format json > vms.json"
	subprocess.call(args, shell=True)


	json_file = open("vms.json", "r")

	data = json.load(json_file)

	if not vmid_list and vmid != None:
		for vm in data:
			if ((vm['id']).replace("qemu/", "")) == vmid:
				return vm['name']
	elif vmid_list and vmid == None:
		name_dictionary = {}
		for vmid in vmid_list:
			for vm in data:
				real_vmid = vm['id'].replace("qemu/", "")
				if real_vmid == vmid:
					name_dictionary[real_vmid] = vm['name']
		return name_dictionary
	else:
		return "Something went wrong"

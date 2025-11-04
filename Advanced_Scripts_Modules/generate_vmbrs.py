#!/usr/bin/env python3
import os

def run():
	f = open("new_interfaces_file.txt", "a+")
	startVMBR = int(input("What did you want the vmbr's to start at? "))
	if startVMBR <= 0:
		print ("Not a valid input")
		return 
	numVMBR = int(input("What is the end vmbr? "))
	if startVMBR > numVMBR:
		print ("Number is not large enough")
		return 
	startIP = input("What is the ip address?")
	for x in range(startVMBR, numVMBR + 1):
		s = "auto vmbr" + str(x) + "\niface vmbr" + str(x) + " inet static\n" + "    address  " + startIP + "\n    netmask  255.255.255.0" + "\n    bridge_ports none" + "\n    bridge_stp off" + "\n    bridge_fd 0\n\n"
		f.write(s)
	f.close()

	return "Success"

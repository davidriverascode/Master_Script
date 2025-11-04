#!/usr/bin/env python3
#qm stop vmid
import subprocess

def run():

	print ("All numbers in digits please")
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to stop NOT CLEAN: ")

	for i in range(int(startvm), (int(endvm)+1)):
	        args = "qm stop " + str(i)
	        print (args)
	        subprocess.call(args, shell=True)

	return "Success"

def stop_machine(vmid):

	args = "qm stop " + str(vmid)
	subprocess.call(args, shell=True)

	return "Success"

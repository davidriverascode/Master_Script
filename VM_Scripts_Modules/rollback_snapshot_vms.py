#!/usr/bin/env python3
#qm snapshot vmid snapname
import subprocess

def run():

	print ("Script for snapshot rollbacks - run when VM is off!")
	print ("All numbers in digits please")
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to rollback: ")
	snapname = input("Enter ROLLBACK Snapshot name (one word only): ")

	for i in range(int(startvm), (int(endvm)+1)):
	        args = "qm rollback " + str(i) + " " + snapname
	        print (args)
	        subprocess.call(args, shell=True)

	return "Success"

#!/usr/bin/env python3
#qm start vmid
import subprocess

def run():

	print ("All numbers in digits please")
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to start: ")

	for i in range(int(startvm), (int(endvm)+1)):
	        args = "qm start " + str(i)
	        print (args)
	        subprocess.call(args, shell=True)

	return "Success"

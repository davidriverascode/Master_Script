#!/usr/bin/env python3
import subprocess

def snapshot_vms_online():

	#qm snapshot vmid snapname

	print("Script for snapshots - run when VM is on!")
	print("All numbers in digits please")
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to snapshot: ")
	snapname = input("Enter Snapshot name (one word only): ")

	for i in range(int(startvm), (int(endvm)+1)):
	        args = "qm snapshot " + str(i) + " " + snapname + " --vmstate 1"
	        print(args)
	        subprocess.call(args, shell=True)

def snapshot_vms_offline():

	#qm snapshot vmid snapname

	print("Script for snapshots - run when VM is off!")
	print("All numbers in digits please")
	startvm = input("Enter start VM Number: ")
	endvm = input("Enter last VM to snapshot: ")
	snapname = input("Enter Snapshot name (one word only): ")

	for i in range(int(startvm), (int(endvm)+1)):
	        args = "qm snapshot " + str(i) + " " + snapname
	        print(args)
	        subprocess.call(args, shell=True)

def run():
	print("Virtual Machine Snapshotting")
	print("\n!! Must be on the same node as VMs !!")
	print("\nIs/are the virtual machine(s) on or off?")
	vm_state = input("Virtual Machine state: ")

	match vm_state:
		case "on" | "On" | "ON":
			snapshot_vms_online()
		case "off" | "Off" | "OFF":
			snapshot_vms_offline()

	return "Success"

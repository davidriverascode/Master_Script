#!/usr/bin/env python3
import os, time, shutil

def run():

	amount_of_devices = input("Would you like to amend a single device or multiple?\n>")

	# Switch statement that checks for different user answers and routes them to the function that they need
	match amount_of_devices:
		case "single" | "Single" | "1" | "Single Device" | "single device" | "Single device":
			amend_single_device()
		case "multiple" | "Multiple" | "Multiple Devices" | "multiple devices" | "Multiple devices":
			amend_multiple_devices()

	return "Success"

def amend_single_device():

	print ("Script to amend a batch of VM network devices, each VM will have the same VMBR")
	path = "/etc/pve/qemu-server/"
	print ("*****")
	startvm = input("Enter first VM Number (e.g. 100): ")
	endvm = input("Enter last VM Number (e.g. 105): ")
	netdevice = input("Enter the network device you want to change (e.g. net0): ")
	vmbrstart = input("Enter the new vmbr number for ALL of these systems (e.g. 2): ")
	totalvms = int(endvm) - int(startvm)
	vmbrend = totalvms + int(vmbrstart)
	#print "End vmbr is calcuated as (last vm - first vm) + start vmbr = " + str(vmbrend)
	print ("*****")
	print ("Startvm = " + startvm)
	print ("EndVM = " + endvm)
	print ("netdevice = " + netdevice)
	print ("New vmbr for ALL systems = " + vmbrstart)
	confirm = input("Correct? [Y/N]")
	if confirm != "Y":
	        print ("Exit as User Request")
	else:
	        backupdir = "/root/BACKUP/conf/"+str(time.time())+"/"
	        if not os.path.exists(backupdir):
	                print ("CREATING BACKUP CONF DIRECTORY", backupdir)
	                os.makedirs(backupdir)
	        vmbrcount = int(vmbrstart)
	        for i in range(int(startvm),int(endvm)+1):
	                fi = path+str(i)+".conf"
	                os.rename(fi, (fi+".bak"))
	                origf = open((fi+".bak"))
	                newf = open(fi, "w+")
	                for lines in origf.readlines():
	                        if lines.startswith(netdevice):
	                                strt = lines.find("vmbr")
	                                newstr = lines[0:strt]+"vmbr"+str(vmbrstart)+"\n"
	                                newf.write(newstr)
	                        else:
	                                newf.write(lines)
	                origf.close()
	                newf.close()
	                newmv = backupdir + str(i) + ".conf.bak"
	                print ("Backing up ", fi, " to " , newmv)
	                shutil.move((fi+".bak"), newmv)
	                vmbrcount+=1

	return "Success"

def amend_multiple_devices():

	# I don't know how this works yet, gotta find it and implement it
	print("Still under development, please use old script")
	return "Still under development, please use old script"

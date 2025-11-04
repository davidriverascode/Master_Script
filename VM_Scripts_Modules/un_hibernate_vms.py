#!/usr/bin/env python3
import os, time, shutil, subprocess

def run():

	print("Script to forcibly remove a hibernation state, e.g. hibernation state keeps timing out on resume.")
	path = "/etc/pve/qemu-server/"
	print("*****")
	startvm = input("Enter first VM Number (e.g. 100): ")
	endvm = input("Enter last VM Number (e.g. 105): ")
	backupdir = "/root/BACKUP/conf/"+str(time.time())+"/"
	if not os.path.exists(backupdir):
	        print("CREATING BACKUP CONF DIRECTORY", backupdir)
	        os.makedirs(backupdir)
	        for i in range(int(startvm),int(endvm)+1):
	                fi = path+str(i)+".conf"
	                os.rename(fi, (fi+".bak"))
	                origf = open((fi+".bak"))
	                newf = open(fi, "w+")
	                issuspended = False
	                foundmostrecentsuspendstate = False
	                vmstatepath = ""
	                for lines in origf.readlines():
	                        if lines.startswith("lock: suspend"):
	                                print("VM is Suspended:",fi)
	                                issuspended = True
	                        elif lines.startswith("vmstate: ") and issuspended == True:
	                                vmstatepath = lines[lines.find(" "):]
	                                print("Found vmstate: " + vmstatepath)
	                                issuspended = False
	                                args = "pvesm free " + vmstatepath
	                                subprocess.call(args, shell=True)
	                        else:
	                                newf.write(lines)
	                origf.close()
	                newf.close()
	                newmv = backupdir + str(i) + ".conf.bak"
	                print("Backing up ", fi, " to " , newmv)
	                shutil.move((fi+".bak"), newmv)

	return "Success"

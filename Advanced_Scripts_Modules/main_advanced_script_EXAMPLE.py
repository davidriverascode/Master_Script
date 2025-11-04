#!/usr/bin/env python3
#from . import create_users, delete_users, add_users, remove_users
#from . import create_vms, delete_vms, start_vms, stop_vms, resume_vms, shutdown_vms, migrate_vms, hibernate_vms, un_hibernate_vms, snapshot_vms, delete_snapshot_vms, rollback_snapshot_vms
from . import generate_vmbrs, find_orphaned_disks, print_out, amend_network_devices, advanced_ceph_commands

def run():
	print("\n\n █   █ █▀▄▀█ █▀▀\n  █ █  █ █ █ ▀▀█\n   ▀   ▀   ▀ ▀▀▀")
	print("--------------------------------------------------------------------")

	print("What would you like to do?\n\n")
	print("1) Generate VMBR(s)\n")

	print("2) Find Orphaned Disks")
	print("3) View Disk In Use")
	print("4) View Disk Orphans")
	print("5) View Disk RBD Output\n")

	print("6) Amend Network Devices\n")

	print("7) Advanced Ceph Commands")

	print("\n\n8) Go back to Master Script")
	print("9) Exit")

	print("\n--------------------------------------------------------------------")
	user_action = input("#) ")
	print("--------------------------------------------------------------------")

	match user_action:
		case "1" | "Generate VMBR" | "Generate VMBRs":
			generate_vmbrs.run()
		case "2" | "Find Orphaned Disks" | "find orphaned disks":
			find_orphaned_disks.run()
		case "3" | "View Disk In Use" | "view disk in use":
			print_out.show("diskinuse.txt") # MAKE THIS PYTHON SCRIPT THAT PRINTS OUTPUT TO SCREEN
		case "4" | "View Disk Orphans" | "view disk orphans":
			print_out.show("view_disk_orphans.txt")
		case "5" | "View Disk RBD Output" | "view disk rbd output":
			print_out.show("view_disk_rbd_output")
		case "6" | "Amend Network Devices" | "amend network devices":
			amend_network_devices.run()
		case "7" | "Advanced Ceph Commands" | "advanced ceph commands":
			advanced_ceph_commands.run()
		case "8" | "Go back to Master Script" | "Go back":
			return
		case "9" | "Exit" | "exit":
			exit()
		case _:
			print("That is not an option bro, try again")

	return "Success"

#!/usr/bin/env python3
#from . import create_users, delete_users, add_users, remove_users
from . import create_vms, delete_vms, start_vms, stop_vms, resume_vms, shutdown_vms, migrate_vms, hibernate_vms, un_hibernate_vms, snapshot_vms, delete_snapshot_vms, rollback_snapshot_vms

def run():
	print("\n\n █   █ █▀▄▀█ █▀▀\n  █ █  █ █ █ ▀▀█\n   ▀   ▀   ▀ ▀▀▀")
	print(" --------------------------------------------------------------------")

	print(" What would you like to do?\n\n")
	print(" 1) Create")
	print(" 2) Destroy\n")

	print(" 3) Start")
	print(" 4) Stop\n")

	print(" 5) Resume")
	print(" 6) Shutdown\n")

	print(" 7) Migrate")
	print(" 8) Hibernate")
	print(" 9) Un-Hibernate\n")

	print(" 10) Snapshot")
	print(" 11) Delete Snapshot")
	print(" 12) Rollback Snapshot\n")

	print("\n\n 13) Go back to Master Script")
	print(" 14) Exit")

	print("\n --------------------------------------------------------------------")
	user_action = input(" > ")
	print("--------------------------------------------------------------------")

	match user_action:
		case "1" | "Create" | "create":
			create_vms.run()

		case "2" | "Delete" | "delete":
			delete_vms.run()

		case "3" | "Start" | "start":
			start_vms.run()

		case "4" | "Stop" | "stop":
			stop_vms.run()

		case "5" | "Resume" | "resume":
			resume_vms.run()

		case "6" | "Shutdown" | "shutdown":
			shutdown_vms.run()

		case "7" | "Migrate" | "migrate":
			migrate_vms.run()

		case "8" | "Hibernate" | "hibernate":
			hibernate_vms.run()

		case "9" | "Un-Hibernate" | "un-hibernate" | "unhibernate":
			un_hibernate_vms.run()

		case "10" | "Snapshot" | "snapshot":
			snapshot_vms.run()

		case "11" | "Delete Snapshot" | "delete snapshot":
			delete_snapshot_vms.run()

		case "12" | "Rollback Snapshot" | "rollback snapshot":
			rollback_snapshot_vms.run()

		case "13" | "Go back to Master Script" | "Go back":
			return
		case "14" | "Exit" | "exit":
			exit()
		case _:
			print("That is not an option bro, try again")

	return "Success"

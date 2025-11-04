#!/usr/bin/env python3
from . import create_users, delete_users, add_users, remove_users, audit_users

def run():
	print("\n\n █  █ █▀▀ █▀▀ █▀▀█ █▀▀ \n █  █ ▀▀█ █▀▀ █▄▄▀ ▀▀█ \n ▀▀▀▀ ▀▀▀ ▀▀▀ ▀ ▀▀ ▀▀▀")
	print(" --------------------------------------------------------------------")

	print(" What would you like to do?\n\n")
	print(" 1) Create user")
	print(" 2) Delete user")
	print(" 3) Add user")
	print(" 4) Remove user")
	print(" 5) Audit users")
	print("\n\n 6) Go back to Master Script")
	print(" 7) Exit")

	print("\n --------------------------------------------------------------------")
	user_action = input(" > ")
	print(" --------------------------------------------------------------------")

	match user_action:
		case "1" | "Create user":
			create_users.run()
		case "2" | "Delete user":
			delete_users.run()
		case "3" | "Add user":
			add_users.run()
		case "4" | "Remove user":
			remove_users.run()
		case "5" | "Audit users":
			audit_users.run()
		case "6" | "Go back to Master Script" | "Go back":
			return
		case "7" | "Exit" | "exit":
			exit()
		case _:
			print("That is not an option bro, try again")

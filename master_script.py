#!/usr/bin/env python3
#from testing import find_vmid_slot_module as find_vmid
from User_Scripts_Modules import main_user_script
from VM_Scripts_Modules import main_vm_script
from Advanced_Scripts_Modules import main_advanced_script

running = True
while running:

	print("\n\n                             Welcome to \n ███ █┼█ ███ ┼┼ █▄┼▄█ ███ ███ ███ ███ ███ ┼┼ ███ ███ ███ ███ ███ ███\n ┼█┼ █▄█ █▄┼ ┼┼ █┼█┼█ █▄█ █▄▄ ┼█┼ █▄┼ █▄┼ ┼┼ █▄▄ █┼┼ █▄┼ ┼█┼ █▄█ ┼█┼\n ┼█┼ █┼█ █▄▄ ┼┼ █┼┼┼█ █┼█ ▄▄█ ┼█┼ █▄▄ █┼█ ┼┼ ▄▄█ ███ █┼█ ▄█▄ █┼┼ ┼█┼")
	print(" ---------------------------------------------------------------------")
	print(" What would you like to do?\n\n")
	print(" 1) Edit users")
	print(" 2) Edit virtual machines")
	print(" 3) Advanced options")
	print("\n\n 4) Exit")
	print(" ---------------------------------------------------------------------")
	user_decision = input(" > ")
	print(" ---------------------------------------------------------------------")

	# Create logic to navigate based off of what the user wants to do
	match user_decision: # python switch statement
		case "1":
			main_user_script.run()
		case "2":
			main_vm_script.run()
		case "3":
			main_advanced_script.run()
		case "4" | "Exit" | "exit":
			running = False

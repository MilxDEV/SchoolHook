# TODO
# Make a 'return' command which goes back to the main menu!
# Try to make BruteForce

import os,sys,time,binascii
import socket

import src.menu_func as menu
from commands import (list_help)



class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
####################################################################

running = True

###################################################################
menu.draw_banner() #Draw the logo as an ASCII
menu.main_menu() # The main menu pop up

#################################################################
# CORE

while running:
    cmd = input(f" {colors.BLUE}> ") #Command line

    if cmd == "help":
        menu.clear_screen()
        list_help.listCommands()
    if cmd == "return":
        menu.clear_screen()
        menu.draw_banner()
        menu.main_menu()
    if cmd == "exit":
        menu.clear_screen()
        menu.exit_scrn()
        running = False
# TODO
# - Make new commands
# - Make the HELP command
# - Joy coding :D:D:D


import os,sys,time,binascii
import socket

import src.menu_func as menu
# from commands import *



class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


menu.draw_banner() #Draw the logo as an ASCII
menu.main_menu() # The main menu pop up

cmd = input(f" {colors.BLUE}> ") #Command line
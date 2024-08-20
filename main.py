import os,ansi,sys,time
import socket

import src.menu_func as menu


class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'




def main():
    menu.draw_banner()
    menu.main_menu()


if __name__ == "__main__":
    main()
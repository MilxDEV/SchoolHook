import os,ansi,time

class colors:
    BLACK = "\033[0;30m"
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    RESET = '\033[0m'


def draw_banner():
    logo = '''
  @@@@@@  @@@@@@@ @@@  @@@  @@@@@@   @@@@@@  @@@     
 !@@     !@@      @@!  @@@ @@!  @@@ @@!  @@@ @@!     
  !@@!!  !@!      @!@!@!@! @!@  !@! @!@  !@! @!!     
     !:! :!!      !!:  !!! !!:  !!! !!:  !!! !!:     
 ::.: :   :: :: :  :   : :  : :. :   : :. :  : ::.: :                                             
      @@@  @@@  @@@@@@   @@@@@@  @@@  @@@            
      @@!  @@@ @@!  @@@ @@!  @@@ @@!  !@@            
      @!@!@!@! @!@  !@! @!@  !@! @!@@!@!             
      !!:  !!! !!:  !!! !!:  !!! !!: :!!             
       :   : :  : :. :   : :. :   :   :::
 '''
    print(colors.RED + logo + colors.RESET)


def main_menu():
    socials = """
 ############################################
 ##  discord.gg/schoolhook                 ##
 ##  DEV(twitter) @MilxTheGoat             ##  
 ############################################   
"""
    print(colors.CYAN + socials + colors.RESET)
    print(f" {colors.BLUE}=================================" + colors.RESET)
    print(colors.RED + " Type 'exit' for exit the program")
    print(colors.RED + " Type 'help' to open the help panel")
    print(f" {colors.BLUE}=================================" + colors.RESET)



def run(command):
    pass
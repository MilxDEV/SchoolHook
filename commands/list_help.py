import binascii

# Colors
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


avaible_commands = {
    "Item1" : False,
    "Item2" : True,
    "Item3" : True,
    "Item4" : False,
    "Item5" : True,
    "Item6" : False,
    "Item7" : True,
    "Item8" : True
}


def setStatus(command_name, is_active):
    if is_active:
        return f"{colors.GREEN}{command_name}{colors.RESET}"
    else:
        return f"{colors.RED}{command_name}{colors.RESET}"

def listCommands():
    print(f"If the command name is {colors.GREEN}GREEN{colors.RESET} then it's available, if it's {colors.RED}RED{colors.RESET} then it's currently unavailable!\n")
    for command_name, is_active in avaible_commands.items():
        print(setStatus(command_name, is_active))
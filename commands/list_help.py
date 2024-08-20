import binascii

# Colors
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


avaible_commands = ["BruteForce(beta)", "HashIT!(beta)"]

def listCommands():
    print(colors.RESET + f"If the command name is {colors.GREEN}GREEN{colors.RESET} then its avaible if its {colors.RED}RED{colors.RESET} then its currently unavaible!\n")
    print(f"{colors.RED} {avaible_commands.pop(0)}")

#!/usr/bin/env python3
import platform
import psutil
import os
import sys

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

os.system('cls' if sys.platform.startswith('win') else 'clear')

print(f"""{Colors.CYAN}
 _______ __   __ _______ _______ _______ _______ _____ __   _ _______  _____ 
 |______   \_/   |______    |    |______ |  |  |   |   | \  | |______ |     |
 ______|    |    ______|    |    |______ |  |  | __|__ |  \_| |       |_____|

{Colors.RESET}                                                                             
""")

def get_system_info():
    print(f"{Colors.GREEN}OS: {Colors.BLUE}{platform.system()}")
    print(f"{Colors.GREEN}Version: {Colors.BLUE}{platform.version()}")
    print(f"{Colors.GREEN}Kernel Version: {Colors.BLUE}{platform.uname().release}")
    print(f"{Colors.GREEN}CPU Information: {Colors.BLUE}{platform.processor()}")
    print(f"{Colors.GREEN}Memory Usage: {Colors.BLUE}{psutil.virtual_memory().used / (1024 ** 3):.2f} GB / {psutil.virtual_memory().total / (1024 ** 3):.2f} GB{Colors.RESET}")

if __name__ == "__main__":
    get_system_info()

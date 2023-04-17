#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script accepts a filename, an IP address, or a server name as input, and tests the connectivity to the specified target
# Scott-20230416: initial version 

# Set up initial variables and imports
import sys
from pinglib import pingthis

# Main routine that is called when script is run
def main():
    user_input = argument_check()
    print("IP, TimeToPing (ms)")
    if file_check(user_input) == 1:
        ping_from_file(user_input)
        sys.exit(0)
    elif file_check(user_input) == 0:
        result = pingthis(user_input)
        print(f"{result[0]}, {result[1]}")

# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if  not len(sys.argv) == 2:
        print("Usage: ping1.py [file | IP Address | Domain Name]")
        sys.exit(1)
    else:
        return sys.argv[1]

def file_check(file_name):
    """Function checks if user input is valid filename"""
    try:
        with open(file_name, 'r') as file:
            return 1
    except FileNotFoundError:
        return 0

def ping_from_file(target_file):
    """Function reads target file, pings targets, and displays results"""
    with open(target_file, 'r') as file:
        for line in file:
            target = line.strip()
            result = pingthis(target)
            print(f"{result[0]}, {result[1]}")

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# a script that will read from a file of computer IPs and names.  It then will ping each one and print the IP or DNS name and the time to ping to the screen

# Scott-20230416: initial version

# Set up initial variables and imports
import sys
from pinglib import pingthis

# Main routine that is called when script is run
def main():
    target_file = argument_check()
    print("IP, TimeToPing (ms)")
    # Open file and do stuff
    with open(target_file, 'r') as file:
        for line in file:
            target = line.strip()
            result = pingthis(target)
            print(f"{result[0]}, {result[1]}")

# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if  not len(sys.argv) == 2:
        print("Usage: ping1.py [file.txt]")
        sys.exit(1)
    else:
        return sys.argv[1]

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

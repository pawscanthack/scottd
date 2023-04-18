#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script accepts log file as argument then returns unique mac addresses with device names containing 'iphone' along with the number of unique MAC addresses
# Returns output to screen and file

# Versioning
# Scott-20230418: initial version

# Set up initial variables and imports
import sys
import datetime
import os
import re


MAC_LIST = []

# Main routine that is called when script is run
def main():
     user_file = argument_check()
     file_check(user_file)
     process_logfile(user_file)
     screen_output()
     file_output()


# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if  len(sys.argv) == 1:
        print("Usage: logs1.py [file]")
        sys.exit(1)
    else:
        return sys.argv[1]

def file_check(file_name):
    """Function checks if user input is valid filename"""
    try:
        with open(file_name, 'r') as file:
            return 1
    except FileNotFoundError:
        sys.exit(1)
    
def process_logfile(logfile):
    """Function iterates through log file searching for 'iphone' and adds unique MAC adresses to list"""
    #print("Process Called")
    with open(logfile, "r") as in_file:
        for line in in_file:
            if "iphone" in line.lower():
                mac_address = re.search("((?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2})", line).group(1)
                if mac_address not in MAC_LIST:
                    MAC_LIST.append(mac_address)
                    
     
def screen_output():
    """Function displays output to screen"""
    for item in MAC_LIST:
        print("\n", item)
    print("\nTotal MAC addresses: %d" % len(MAC_LIST))
     
def file_output():
    """Function writes to output to file"""
    filename = get_filename()
    with open(filename, 'w') as file:
        for item in MAC_LIST:
            file.write("%s\n" % item)
        file.write("Total MAC addresses: %d" % len(MAC_LIST))
    print(f'\nOutput saved in {filename}')
    

def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'{script_name}_{now}.txt'



# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

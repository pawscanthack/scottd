#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script accepts log file as argument then returns unique mac addresses with device names containing 'iphone' along with the number of unique MAC addresses
# Returns output to screen and csv

# Versioning
# Scott-20230418: initial version

# Set up initial variables and imports
import sys
import datetime
import os
import re
import csv

CLIENT_DICT = {}

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
        print("Usage: logs2.py [file]")
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
    """Function iterates through log file"""
    print("Process Called")
    with open(logfile, "r") as in_file:
        for line in in_file:
            ack = ack_check(line)
            key = extract_key(line)
            if key in CLIENT_DICT:
                CLIENT_DICT[key] += ack
            else:
                CLIENT_DICT[key] = ack
            
     
def screen_output():
    """Function displays output to screen"""
    print(CLIENT_DICT)

def file_output():
    """Function writes to output to csv file"""
    filename = get_filename()
    with open(filename, 'w') as file:
        for key in CLIENT_DICT:
            file.write("%s,%s\n"%(key, CLIENT_DICT[key]))
    print(f'\nOutput saved in {filename}')
    

def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'ProblemMacs_{now}.csv'

def ack_check(entry):
    # Return 1 if ack code is present
    return 1

def extract_key(entry):
    # Return IP-MAC key value
    ip_address_match = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", entry)
    mac_address_match = re.search("((?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2})", entry)
    
    if ip_address_match and mac_address_match:
        ip_address = ip_address_match.group()
        mac_address = mac_address_match.group()
        extracted_key = mac_address + "," + ip_address
        return extracted_key
    else:
        # Handle the case where a match was not found
        return None

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

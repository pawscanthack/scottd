#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script accepts log file as argument then returns top two MAC/IPs by ACK #
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
    print("\nTop 2 MAC/IP by ACK Requests:\n")
    print(f"{'MAC Address':<20} {'IP Address':<20} {'ACK Total':<10}")
    print("-" * 50)
    top_two = sorted(CLIENT_DICT.items(), key=lambda item: item[1], reverse=True)[:2]
    for key, value in top_two:
        mac, ip = key.split(",")
        print(f"{mac:<20} {ip:<20} {value:<10}")


def file_output():
    """Function writes to output to csv file"""
    filename = get_filename()
    largest_key1 = max(CLIENT_DICT, key=lambda k: CLIENT_DICT[k] or 0)
    largest_key2 = max((k for k in CLIENT_DICT if k != largest_key1), key=lambda k: CLIENT_DICT[k] or 0)
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['MAC', 'IP', 'ACK TOTAL'])
        mac1, ip1 = largest_key1.split(',')
        mac2, ip2 = largest_key2.split(',')
        csv_writer.writerow([mac1, ip1, CLIENT_DICT[largest_key1]])
        csv_writer.writerow([mac2, ip2, CLIENT_DICT[largest_key2]])
    print(f'\nOutput saved in {filename}')


def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'ProblemMacs_{now}.csv'

def ack_check(entry):
    # Return 1 if ack code is present
    if "DHCPACK" in entry:
        return 1
    else:
        return 0

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

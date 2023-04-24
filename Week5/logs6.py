#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script will search for an IP in the a connections to a mail server from a log file
# Returns server name ip, and from address to screen and csv

# Versioning
# Scott-20230420: initial version
# Scott-20230423: v2
# Fixed script to show from addresses correctly

# Set up initial variables and imports
import sys
import datetime
import os
import re
import csv
import time
import re


# Main routine that is called when script is run
def main():
    argument_check()
    file_check(sys.argv[1])
    log_list = create_list_from_file(sys.argv[1])
    result_dict = process_log(log_list)
    screen_output(result_dict)
    file_output(result_dict)


# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if len(sys.argv) == 1:
        print("Usage: maillog.py [log file]")
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

def create_list_from_file(logfile):
    """Function accepts a file and returns a list"""
    newlist = []
    with open(logfile, 'r') as file:
        for line in file:
            newlist.append(line.strip())
        return newlist


def process_log(loglist):
    """Function receives a logfile in a list and returns a dictionary of server name, ip adresses, and from addresses for connecting servers"""
    server_dict = {}
    for line in loglist:
        if "connect" in line:
            match = re.search(r' connect from (\S+)\[(\d+\.\d+\.\d+\.\d+)\]', line)
            if match:
                server_name = match.group(1)
                ip_address = match.group(2)
                #from_domain = re.search(r'(\S+)\.\S+\[\d+\.\d+\.\d+\.\d+\]', line).group(1)
                index = loglist.index(line)
                from_line = loglist[index+3]
                match = re.search(r'from=<([^>]+)>', from_line)
                if match:
                    email_address = match.group(1)
                server_dict.update({server_name:[ip_address, email_address]})
            
    return server_dict


def screen_output(dict):
    """Function displays dictionary to screen"""
    print()
    header = f"{'SERVER NAME':<25} {'IP ADDRESS':<15} {'FROM':<25}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for key, value in dict.items():
        servername = key
        ip = value
        row = f"{key:<25} {value[0]:<15} {value[1]:<25}"
        print(row)


def file_output(dict):
    """Function writes dictionary to csv file"""
    filename = get_filename()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['SERVER_NAME', 'IP_ADDRESS', 'FROM']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in dict.items():
            row_dict = {'SERVER_NAME': key, 'IP_ADDRESS': value[0], 'FROM': value[1]}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    script_name = sys.argv[0].split('/')[-1]  # get script name from command line arguments
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'{script_name}_{now}.csv'


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script will search for an IP in the a connections to a mail server from a log file
# Returns server name and ip  to screen and csv

# Versioning
# Scott-20230420: initial version

# Set up initial variables and imports
import sys
import datetime
import os
import re
import csv
import requests
import time


DEFAULT_LOG = "dhcpdsmall.log"

# Main routine that is called when script is run
def main():
    argument_check()
    file_check(sys.argv[1])
    result_list = process_log(sys.argv[1])
    screen_output(result_list)
    #file_output(result_list)


# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if len(sys.argv) == 1:
        # Future Feature: accept optional third argument for log file later
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

def process_log(logfile):
    server_list = ['1.1.1.1', 'super_secret_server.net' ]
    with open(logfile, "r") as file:
        for line in file:
            if "connect" in line:
                print("found")
    return server_list


def screen_output(list):
    """Function displays disctionary to screen"""
    print()
    header = f"{'SERVER NAME':<15} {'IP ADDRESS':<18}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for item in list:
        row = f"{item[0]:<15} {item[1]:<18}"
        print(row)


def file_output(list):
    """Function writes dictionary to csv file"""
    filename = get_filename()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP', 'MAC ADDRESS', 'VENDOR']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in dict.items():
            row_dict = {'IP': key, 'MAC ADDRESS': value[0], 'VENDOR': value[1]}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'logs3_{now}.csv'


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

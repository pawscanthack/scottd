#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script will search a log file for redirects
# Returns count, from, and to to csv file and screen output

# Versioning
# Scott-20230420: initial version

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
    result_dict = process_log(sys.argv[1])
    screen_output(result_dict)
    #file_output(result_dict)


# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if len(sys.argv) == 1:
        print("Usage: logs5.py [log file]")
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
    """Function receives log file and returns a dictionary of count, from, and to for redirects"""
    redirect_dict = {}
    with open(logfile, "r") as file:
        for line in file:
            if "ActiveSync" in line or "Basic" in line:
                print("Skipped")
                continue
            if "REDIRECT" in line:
                print("Redirect found")
                match = re.search(r'REDIRECT: (.*) to (https?://\S+)', line)
                if match:
                    from_value = match.group(1)
                    to_value = match.group(2)
                    print(f"From: {from_value}")
                    print(f"To: {to_value}")
                    if from_value in redirect_dict and redirect_dict[from_value][0] == to_value:
                        redirect_dict[from_value][1] += 1
                    else:
                        redirect_dict.update({from_value: [to_value, 1]})
                else:
                    print("Not Found")
    return redirect_dict


def screen_output(dict):
    """Function displays dictionary to screen"""
    print(dict)
    header = f"{'COUNT':<10} {'FROM':<50} {'TO':<50}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for key, value in dict.items():
        from_value = key
        to_value  = value[0]
        count_value = value[1]
        row = f"{count_value:<10} {from_value:<50} {to_value:<50}"
        print(row)


def file_output(dict):
    """Function writes dictionary to csv file"""
    filename = get_filename()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['SERVER_NAME', 'IP_ADDRESS']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in dict.items():
            row_dict = {'SERVER_NAME': key, 'IP_ADDRESS': value}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'maillog.py_{now}.csv'


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

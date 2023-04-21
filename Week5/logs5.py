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
    file_output(result_dict)


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
                continue
            if "REDIRECT" in line:
                match = re.search(r'REDIRECT: (.*) to (https?://\S+)', line)
                if match:
                    from_value = match.group(1)
                    to_value = match.group(2)
                    if from_value in redirect_dict and redirect_dict[from_value][0] == to_value[:-2]:
                        redirect_dict[from_value][1] += 1
                    else:
                        redirect_dict.update({from_value: [to_value[:-2], 1]})
    return redirect_dict


def screen_output(dict):
    """Function displays dictionary to screen"""
    print()
    header = f"{'COUNT':<10} {'FROM':<25} {'TO':<75}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for key, value in dict.items():
        from_value = key
        to_value  = value[0]
        count_value = value[1]
        row = f"{count_value:<10} {from_value:<25} {to_value:<75}"
        print(row)


def file_output(dict):
    """Function writes dictionary to csv file"""
    filename = get_filename()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['COUNT', 'TO', 'FROM']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in dict.items():
            row_dict = {'COUNT': value[1], 'TO':value[0], 'FROM': key}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'logs5.py_{now}.csv'


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

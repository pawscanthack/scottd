#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script that detect the OS scan over the hosts found in nmap1
# Creates a CSV of the IPs and open ports with additional OS info
# Must be run as 'sudo'

# Versioning
# Scott-20230427: initial version

# Set up initial variables and imports
import sys
import nmap3
import csv
import datetime

DEFAULT_TARGET_FILE = 'nmap1.csv'


# Main routine that is called when script is run
def main():
    target_dictionary = read_file_to_dictionary(DEFAULT_TARGET_FILE)
    scan_results = scan_target_dictionary(target_dictionary)
    print(scan_results)
    #file_output(scan_results)
    #screen_output(target_dictionary)
    #print(target_dictionary)

# Subroutines
def read_file_to_dictionary(filename):
    """Function accepts filename and returns dictionary"""
    result = {}
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        for row in reader:
            key = row['IP_ADDRESS']
            value = row['PORTS']
            result[key] = value
    return result

def scan_target_dictionary(target_dict):
    """Functions accepts dictionary, uses nmap os detection on from IPs from key values, returns updated dictionary with OS info appended"""
    updated_dict = {}
    for key, value in target_dict.items():
        os_info = get_os_info(key)
        updated_entry = [value, os_info]
        updated_dict[key] = updated_entry
    return updated_dict 

def get_os_info(ip):
    """Function accepts ip address and returns os info"""
    nmap = nmap3.Nmap()
    os_results = nmap.nmap_os_detection(ip)
    #print(os_results)
    os_match = os_results[ip]['osmatch'][0]['name']
    return os_match

def screen_output(scan_dict):
    """Function displays dictionary to screen"""
    print()
    header = f"{'IP ADDRESS':<25} {'PORTS':<15}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for key, value in scan_dict.items():
        ports_list = value.split()  # Split the value string into a list of strings
        ports = ' '.join(ports_list)  # Join the list of strings with a single space
        row = f"{key:<25} {ports:<15}"
        print(row)


def file_output(scan_dict):
    """Function writes dictionary to csv file"""
    #FIX: Update format with new row for OS info
    #filename = get_filename()
    filename = 'nmap1.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP_ADDRESS', 'PORTS']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in scan_dict.items():
            row_dict = {'IP_ADDRESS': key, 'PORTS': ' '.join(map(str, value))}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

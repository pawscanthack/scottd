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
    #target_file = argument_check()
    #file_check(target_file)
    target_dictionary = read_file_to_dictionary(DEFAULT_TARGET_FILE)
    scan_results = scan_target_dictionary(target_dictionary)
    print(scan_results)
    #file_output(scan_results)
    #screen_output(scan_results)


# Subroutines
def argument_check():
    #FIX: return DEFAULT_TARGET_FILE if none is passed in command line
    """Function checks for presence of argument and gives usage if argument is missing"""
    if  len(sys.argv) == 1:
        # FIX Usage info
        print("Usage: nmap2.py [file]")
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

def read_file_to_dictionary(file):
     """Function accepts filename and returns dictionary"""

def scan_target_dictionary(target_dict):
     """Functions accepts dictionary, scans targets from key values, return dictionary with OS info appended"""

def get_os_info(ip):
     """Function accepts ip address and returns os info"""

""" def scan_target_list(target_list):
    #Function accepts list of targets and performs syn scan on each, returning the results as a dictionary
    result = {}
    nmap = nmap3.NmapScanTechniques()
    for target in target_list:
        scan_data = nmap.nmap_syn_scan(target, args="-T5")  # Perform syn scan on the target
        #scan_data = nmap.nmap_syn_scan(target, "1-65535")  # Perform syn scan on full range of ports
        result[target] = scan_data  # Update the result dictionary with the scan data
    return result """


""" def filter_scan_result(filter_dict):
    #Function accepts dictionary output from nmap scan and returns dictionary of IPs and open ports
    return_dict = {}
    for main_key, nested_dict in filter_dict.items():    
        ip_address_key = list(nested_dict.keys())[0]
        # Iterate through the 'ports' list
        for ip_address_key, ip_info in nested_dict.items():
            if 'ports' in ip_info:
                for port_info in ip_info['ports']:
                    # Check if the 'state' is 'open'
                    if port_info['state'] == 'open':
                        #print(f"Port {port_info['portid']} is open.")
                        port = port_info['portid']
                        if ip_address_key not in return_dict:
                            return_dict[ip_address_key] = [port]
                        else:
                            return_dict[ip_address_key].append(port)
                    else:
                        #print(f"Port {port_info['portid']} is not open (state: {port_info['state']}).")
                        continue
    return return_dict """


def screen_output(scan_dict):
    """Function displays dictionary to screen"""
    #FIX: Update format with new row for OS info
    print()
    header = f"{'IP ADDRESS':<25} {'PORTS':<15}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for key, value in scan_dict.items():
        row = f"{key:<25} {' '.join(map(str, value)):<15}"
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

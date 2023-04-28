#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script that does a syn scan of DEFAULT_TARGETS(152.157.64.0/24 and 152.157.65.0/24)
# Creates a CSV of the IPs and open ports
# Must be run as 'sudo'

# Versioning
# Scott-20230427: initial version

# Set up initial variables and imports
import sys
import nmap3
import csv
import datetime

DEFAULT_TARGET_LIST =['152.157.64.0/24', '152.157.65.0/24']
#DEFAULT_TARGET_LIST =['scanme.nmap.org']


# Main routine that is called when script is run
def main():
    scan_result = scan_target_list(DEFAULT_TARGET_LIST)
    filtered_result = filter_scan_result(scan_result)
    file_output(filtered_result)
    screen_output(filtered_result)


# Subroutines
def scan_target_list(target_list):
    """Function accepts list of targets and performs syn scan on each, returning the results as a dictionary"""
    result = {}
    nmap = nmap3.NmapScanTechniques()
    for target in target_list:
        scan_data = nmap.nmap_syn_scan(target, args="-T5")  # Perform syn scan on the target
        #scan_data = nmap.nmap_syn_scan(target, "1-65535")  # Perform syn scan on full range of ports
        result[target] = scan_data  # Update the result dictionary with the scan data
    return result


def filter_scan_result(filter_dict):
    """Function accepts dictionary output from nmap scan and returns dictionary of IPs and open ports"""
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
    return return_dict


def screen_output(scan_dict):
    """Function displays dictionary to screen"""
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
    filename = get_filename()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP_ADDRESS', 'PORTS']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in scan_dict.items():
            row_dict = {'IP_ADDRESS': key, 'PORTS': ' '.join(map(str, value))}
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

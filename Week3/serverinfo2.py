#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# This script returns information about the machine it is running to an ouput method specified by passing an argument to the command. 
# This argument can be 'screen', 'csv', or 'json'. 

# Versioning
# Scott-20230412: initial version

# Set up initial variables and imports
import socket
import platform
import psutil
import netifaces
import os
import sys
import json
import csv
import datetime

# Main routine that is called when script is run
def main():
    # Check to see if the user passed an argument
    if len(sys.argv) > 1:
        output_method = sys.argv[1]
    else:
        output_method = 'screen'

    # Gather the data
    system_info = gather_data()

    # Print the results to the correct output method
    if output_method == 'screen':
        output_to_screen(system_info)
    elif output_method == 'csv':
        output_to_csv(system_info)
    elif output_method == 'json':
        output_to_json(system_info)
    else:
        print('Invalid output method.  Valid options are screen, csv, and json')    


# Subroutines

def gather_data():
    """
    Function to gather the data and return it as a dictionary"""
     # Retrieve the hostname
    hostname = socket.gethostname()

    # Retrieve the IP address and MAC address of the 'eth0' interface
    ip_address = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
    mac_address = netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']

    # Retrieve the number of CPUs and amount of RAM
    cpus = str(os.cpu_count())
    ram_gb = str(round(psutil.virtual_memory().total / (1024.0 ** 3)))

    # Retrieve the operating system type and version
    os_type = platform.system()
    os_version = platform.release()

    # Retrieve the number of disks
    disk_count = str(len(psutil.disk_partitions()))

    # Create a dictionary to store the results
    system_info = {
        'Hostname': hostname,
        'CPU (count)': cpus,
        'RAM (GB)': ram_gb,
        'OSType': os_type,
        'OSVersion': os_version,
        'Disks (Count)': disk_count,
        'ip of eth0': ip_address,
        'mac of eth0': mac_address
    }
    return system_info

def output_to_screen(system_info):
    """Function to print the data to the screen"""
    print()
    for key, value in system_info.items():
        print(f'{key}: {value}')

def output_to_csv(system_info):
    """Function to print the data to a CSV file"""
    output_file = get_filename('csv')
     # Write the dictionary to the CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=system_info.keys())
        writer.writeheader()
        writer.writerow(system_info)

def output_to_json(system_info):
    """Function to print the data to a JSON file"""
    output_file = get_filename('json')
    # Write the dictionary to the JSON file
    with open(output_file, 'w') as jsonfile:
        json.dump(system_info, jsonfile)


def get_filename(type):
    """Function to generate a filename based on the script name and the current date and time"""
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'{script_name}_{now}.{type}'

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

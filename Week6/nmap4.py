#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script that takes a csv file of IP and DNS info and adds additional columns for Country, RegionName, City, Zipcode, ISP
# Results output to csv file and screen

# Versioning
# Scott-20230430: initial version

# Set up initial variables and imports
import nmap3
import csv
import requests
import json

DEFAULT_TARGET_FILE = 'nmap3a.csv'


# Main routine that is called when script is run
def main():
    target_dictionary = read_file_to_dictionary(DEFAULT_TARGET_FILE)
    updated_dictionary = process_target_dictionary(target_dictionary)
    #csv_output(scan_results)
    #screen_output(scan_results)
    print(updated_dictionary)

# Subroutines
def read_file_to_dictionary(filename):
    """Function accepts filename and returns dictionary"""
    result = {}
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        for row in reader:
            key = row['IP']
            value = row['DNS']
            result[key] = {'IP': key, 'DNS': value}
    return result

def process_target_dictionary(target_dict):
    """Functions accepts dictionary, uses nmap os detection on targets from key values, returns updated dictionary with OS info appended"""
    for key, value in target_dict.items():
        api_info = call_api(key)
        parsed_info = json.loads(api_info)
        target_dict[key].update(parsed_info)
    return target_dict 

def call_api(target):
    """Function to call macvendor API"""
    url = f"http://ip-api.com/json/{target}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error for target '{target}': status code {response.status_code}, response text '{response.text}'")
        return "Not Found"

def screen_output(scan_dict):
    """Function displays dictionary to screen"""
    print()
    header = f"{'IP ADDRESS':<25} {'PORTS':<15} {'OS INFO':<15}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for key, value in scan_dict.items():
        ip_address = value['IP_ADDRESS']
        ports_list = value['PORTS'].split()  # Split the value string into a list of strings
        ports = ' '.join(ports_list)  # Join the list of strings with a single space
        os_info = value['OS_INFO']
        row = f"{ip_address:<25} {ports:<15} {os_info:<15}"
        print(row)

def csv_output(scan_dict):
    """Function writes dictionary to csv file"""
    filename = 'nmap2.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP_ADDRESS', 'PORTS', 'OS_INFO']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in scan_dict.items():
            row_dict = {'IP_ADDRESS': value['IP_ADDRESS'], 'PORTS': value['PORTS'], 'OS_INFO': value['OS_INFO']}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

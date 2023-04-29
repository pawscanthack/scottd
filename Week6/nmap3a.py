#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script runs an nmap dns brute scan against nsd.org and put the DNS names and IP's into a csv file

# Versioning
# Scott-20230429: initial version

# Set up initial variables and imports
import nmap3
import csv

DEFAULT_TARGET = 'nsd.org'

# Main routine that is called when script is run
def main():
    result_dict = scan_target(DEFAULT_TARGET)
    #screen_output(result_dict)
    #csv_output(result_dict)
    print(result_dict)
    
# Subroutines
def scan_target(target):
    """Functions accepts target, uses nmap dns brute force on target, returns dictionary with DNS info"""
    updated_dict = {}
    dns_info = scan_dns(target)
    updated_dict['DNS_INFO'] = dns_info
    return updated_dict 

def scan_dns(target):
    """Function accepts target and returns os info"""
    nmap = nmap3.Nmap()
    dns_results = nmap.nmap_dns_brute_script(target)
    #FIX
    #dns_match = dns_results[target]['osmatch'][0]['name']
    return dns_results

""" def screen_output(scan_dict):
    #Function displays dictionary to screen
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
    #Function writes dictionary to csv file
    filename = 'nmap2.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP_ADDRESS', 'PORTS', 'OS_INFO']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in scan_dict.items():
            row_dict = {'IP_ADDRESS': value['IP_ADDRESS'], 'PORTS': value['PORTS'], 'OS_INFO': value['OS_INFO']}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}') """

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

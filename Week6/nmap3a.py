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
    result_list = scan_dns(DEFAULT_TARGET)
    screen_output(result_list)
    #csv_output(result_dict)
    print(result_list)
    
# Subroutines
def scan_dns(target):
    """Function accepts target and returns os info"""
    nmap = nmap3.Nmap()
    dns_results = nmap.nmap_dns_brute_script(target)
    print(type(dns_results))
    return dns_results

def screen_output(scan_list):
    #Function displays list of dictionaries to screen
    print()
    header = f"{'address':<25} {'hostname':<15}"
    print(header)
    print('-' * len(header))
    # Loop through list of dictionaries displaying content to screen
    for scan_dict in scan_list:
        ip_address = scan_dict['address']
        host = scan_dict['hostname']
        row = f"{ip_address:<25} {host:<15}"
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
    print(f'\nOutput saved in {filename}')

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script runs an nmap dns brute scan against nsd.org and put the DNS names and IP's into a csv file

# Scott-20230429: initial version

# Set up initial variables and imports
import nmap3
import csv

DEFAULT_TARGET = 'nsd.org'

# Main routine that is called when script is run
def main():
    result_list = scan_dns(DEFAULT_TARGET)
    filtered_list = filter_list(result_list)
    screen_output(filtered_list)
    csv_output(filtered_list)

    
# Subroutines
def scan_dns(target):
    """Function accepts target and returns os info"""
    nmap = nmap3.Nmap()
    dns_results = nmap.nmap_dns_brute_script(target)
    return dns_results


def filter_list(scan_list):
    """Function prunes IPv6 Info from list"""
    pruned_list = []
    for scan_dict in scan_list:
        ip_address = scan_dict['address']
        if ':' not in ip_address:
            pruned_list.append(scan_dict)
    return pruned_list


def screen_output(scan_list):
    """Function displays list of dictionaries to screen"""
    print()
    header = f"{'IP':<25} {'DNS':<15}"
    print(header)
    print('-' * len(header))
    # Loop through list of dictionaries displaying content to screen
    for scan_dict in scan_list:
        ip_address = scan_dict['address']
        host = scan_dict['hostname']
        row = f"{ip_address:<25} {host:<15}"
        print(row)


def csv_output(scan_list):
    """Function writes list of dictionaries to csv file"""
    filename = 'nmap3a.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP', 'DNS']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for scan_dict in scan_list:
            row_dict = {'IP': scan_dict['address'], 'DNS': scan_dict['hostname']}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

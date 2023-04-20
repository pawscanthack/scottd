#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# script will search for an IP in the a log file (default:dhcpdsmall.log), get the mac address and then lookup the mac address vendor at https://api.macvendors.com/
# Returns output to screen and csv

# Versioning
# Scott-20230420: initial version

# Set up initial variables and imports
import sys
import datetime
import os
import re
import csv
import requests
import time


DEFAULT_LOG = "dhcpdsmall.log"

# Main routine that is called when script is run
def main():
    argument_check()
    target_file = file_check(sys.argv[1])
    log_file = file_check(DEFAULT_LOG)
    ip_dict = build_dict(target_file)
    ip_mac_dict = extract_mac_address(DEFAULT_LOG, ip_dict)
    results_dict = get_vendor(ip_mac_dict)
    screen_output(results_dict)
    file_output(results_dict)


# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if len(sys.argv) == 1:
        # Future Feature: accept optional third argument for log file later
        print("Usage: logs3.py [target file]")
        sys.exit(1)
    else:
        return sys.argv[1]


def file_check(file_name):
    """Function checks if user input is valid filename"""
    try:
        with open(file_name, 'r') as file:
            return file_name
    except FileNotFoundError:
        sys.exit(1)


def build_dict(targetfile):
    """Function creates dictionary of ip addresses from file"""
    results = {}
    with open(targetfile) as tf:
        content = tf.read().splitlines()
        for ip in content:
            results[ip] = [None, None]
    return results


def extract_mac_address(logfile, target_dict):
    """Function to get MAC addresses from dictionary of IP addresses and logfile, appending MAC value to IP key in dictionary"""
    with open(logfile, "r") as file:
        # Iterate through log file by line
        for line in file:
            # Iterate through dictionary of ip addresses
            for key in target_dict:
                # Check for IP address in line from log file
                if key in line:
                    mac_address_match = re.search("((?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2})", line)
                    if mac_address_match:
                        mac_address = mac_address_match.group()
                        target_dict[key] = [mac_address, None]
    return target_dict


def get_vendor(ipmac_dict):
    """Function to add vendors to dictionary"""
    ip_mac_vendor_dict = ipmac_dict.copy()
    # Loop through dictionary items adding vendor info
    for ip, (mac, _) in ipmac_dict.items():
        vendor = api_call(mac)
        ip_mac_vendor_dict[ip] = [mac, vendor]
    return ip_mac_vendor_dict


def api_call(mac):
    """Function to call macvendor API"""
    # Necessary delay for free API calls
    delay = .75
    time.sleep(delay)
    url = f"https://api.macvendors.com/{mac}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error for MAC '{mac}': status code {response.status_code}, response text '{response.text}'")
        return "Not Found"


def screen_output(dict):
    """Function displays disctionary to screen"""
    print()
    header = f"{'IP':<15} {'MAC ADDRESS':<18} {'VENDOR'}"
    print(header)
    print('-' * len(header))
    # Loop through dictionary displaying content to screen
    for key, value in dict.items():
        ip = key
        mac_address = value[0]
        vendor = value[1]
        row = f"{ip:<15} {mac_address:<18} {vendor}"
        print(row)


def file_output(dict):
    """Function writes to dictionary to csv file"""
    filename = get_filename()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP', 'MAC ADDRESS', 'VENDOR']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for key, value in dict.items():
            row_dict = {'IP': key, 'MAC ADDRESS': value[0], 'VENDOR': value[1]}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


def get_filename():
    """Function to generate a filename based on the script name and the current date and time"""
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return f'logs3_{now}.csv'


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

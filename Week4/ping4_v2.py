#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script accepts a filename, an IP address, or a server name as input, and tests the connectivity to the specified target plus takes an optional second command line argument that is a csv output file
# Scott-20230416: initial version 

# Set up initial variables and imports
import sys
from pinglib import pingthis
import csv
import socket

csv_output = []

# Main routine that is called when script is run
def main():
    user_input = argument_check()
    filename = csv_check()
    print("IP".ljust(20) + "Domain Name".ljust(30) + "TimeToPing (ms)")
    if file_check(user_input) == 1:
        ping_from_file(user_input, filename)
        sys.exit(0)
    elif file_check(user_input) == 0:
        result = pingthis(user_input)
        target_dns = get_domain(result[0])
        ping_result = [result, target_dns]
        csv_output.append(ping_result)
        print(f"{result[0].ljust(20)}{target_dns.ljust(30)}{result[1]}")
        if filename != 0:
            write_to_csv(filename)

# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if  len(sys.argv) == 1:
        print("Usage: ping1.py [file | IP Address | Domain Name]")
        sys.exit(1)
    else:
        return sys.argv[1]

def file_check(file_name):
    """Function checks if user input is valid filename"""
    try:
        with open(file_name, 'r') as file:
            return 1
    except FileNotFoundError:
        return 0

def ping_from_file(target_file, filename):
    """Function reads target file, pings targets, and displays results"""
    with open(target_file, 'r') as file:
        for line in file:
            target = line.strip()
            result = pingthis(target)
            target_dns = get_domain(target)
            ping_result = [result, target_dns]
            csv_output.append(ping_result)
            print(f"{result[0].ljust(20)}{target_dns.ljust(30)}{result[1]}")
            if filename != 0:
                write_to_csv(filename)

def csv_check():
    """Function checks for filename argument"""
    if len(sys.argv) == 3:
        return sys.argv[2]
    else:
        return 0

def write_to_csv(filename):
    """Function writes content to CSV file"""
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in csv_output:
            csv_writer.writerow([str(item) for item in row])
    return

def get_domain(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        domain_name = "Unknown"
    return domain_name

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

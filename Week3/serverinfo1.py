#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# This script returns information about the machine it is running on to the screen

# Versioning
# Scott-20230412: initial version

# Set up initial variables and imports
import socket
import platform
import psutil
import netifaces
import os

# Main routine that is called when script is run
def main():

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

    # Get the list of disk partitions
    partitions = psutil.disk_partitions()

    # Get the list of unique device names
    devices = set(partition.device for partition in partitions)

    # Count the number of devices
    num_disks = len(devices)

    # Create a dictionary to store the results
    system_info = {
        'Hostname': hostname,
        'CPU (count)': cpus,
        'RAM (GB)': ram_gb,
        'OSType': os_type,
        'OSVersion': os_version,
        'Disks (Count)': num_disks,
        'ip of eth0': ip_address,
        'mac of eth0': mac_address
    }

    # Print the results
    print()
    for key, value in system_info.items():
        print(f'{key}: {value}')


# Subroutines


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

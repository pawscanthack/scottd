#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# This script returns information about the machine it is running on to the screen and saves it to a database

# Versioning
# Scott-20230506: initial version (developed from serverinfo1.py)

# Set up initial variables and imports
import socket
import platform
import psutil
import netifaces
import os
import subprocess
import pymysql

DB_LOCATION = '44.205.160.194'
DB_USER = 'cmdb'
DB_NAME = 'cmdb'
DB_PASS = 'cmdbpass'
TABLE_NAME = 'devices'


# Main routine that is called when script is run
def main():
    system_info = get_system_info()
    db_connection = create_db_connection(DB_LOCATION, DB_USER, DB_PASS, DB_NAME)
    systeminfo = get_system_info()
    screen_output(systeminfo)
    write_to_db(db_connection, system_info)


# Subroutines
def get_system_info():
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
    proc = subprocess.run("lsblk | grep disk | wc -l", shell=True, universal_newlines=True, capture_output=True, text=True) 
    num_disks = proc.stdout.strip()

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

    return system_info

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error: '{err}'")

    return connection


def screen_output(dict_data):
    """Function displays dictionary to screen"""
    print()
    header = f"{'NAME':<20} {'MAC':<20} {'IP':<15} {'CPU_COUNT':<10} {'DISKS':<10} {'RAM':<10} {'OSTYPE':<15} {'OSVERSION':<15}"
    print(header)
    print('-' * len(header))
    
    name = dict_data['Hostname']
    mac = dict_data['mac of eth0']
    ip = dict_data['ip of eth0']
    cpu = dict_data['CPU (count)']
    disks = dict_data['Disks (Count)']
    ram = dict_data['RAM (GB)']
    ostype = dict_data['OSType']
    osversion = dict_data['OSVersion']
    
    row = f"{name:<20} {mac:<20} {ip:<15} {cpu:<10} {disks:<10} {ram:<10} {ostype:<15} {osversion:<15}"
    print(row)


def write_to_db(connection, dict_data):
    cursor = connection.cursor()
    name = dict_data['Hostname']
    mac = dict_data['mac of eth0']
    ip = dict_data['ip of eth0']
    cpu = int(dict_data['CPU (count)'])
    disks = int(dict_data['Disks (Count)'])
    ram = int(dict_data['RAM (GB)'])
    ostype = dict_data['OSType']
    osversion = dict_data['OSVersion']
    sql = "INSERT INTO devices(name, macaddress, ip, cpucount, disks, ram, ostype, osversion) \
    VALUES ('%s', '%s', '%s', '%d', '%d', '%d', '%s', '%s')" % (name, mac, ip, cpu, disks, ram, ostype, osversion)
    try:
        cursor.execute(sql)
        connection.commit()
    except:
        db.rollback
    connection.close()
    return


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

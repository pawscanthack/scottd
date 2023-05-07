#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script connects to a database and prints out the data in the rows to csv and json formatted files

# Versioning
# Scott-20230506: initial version

# Set up initial variables and imports
import sys
import pymysql
import json
import csv


DB_LOCATION = '44.205.160.194'
DB_USER = 'cmdb'
DB_NAME = 'cmdb'
DB_PASS = 'cmdbpass'
TABLE_NAME = 'devices'


# Main routine that is called when script is run
def main():
    file_output_type = argument_check()
    data_list = get_data()
    screen_output(data_list)

    # Print the results to the correct output method
    if file_output_type == 'csv':
        csv_output(data_list)
    elif file_output_type == 'json':
        json_output(data_list)
    else:
        print('Invalid output method.  Valid options are csv, and json')


# Subroutines
def argument_check():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if  not len(sys.argv) == 2:
        print("Usage: database2.py [csv || json]")
        sys.exit(1)
    else:
        #FIX: Add error handling
        return sys.argv[1]


def get_data():
    """Function connects to database and returns data as a list"""
    # Create list
    new_list = []
    # Open database connection
    db = pymysql.connect(host=DB_LOCATION, user=DB_USER, password=DB_PASS, database=DB_NAME)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM devices "
    try:
      # Execute the SQL command
      cursor.execute(sql)
      # Fetch all the rows in a list of lists.
      results = cursor.fetchall()
      for row in results:
          name = row[0]
          macaddress = row[1]
          ip = row[2]
          cpucount = row[3]
          disks = row[4]
          ram = row[5]
          ostype = row[6]
          osversion = row[7]
          # Now print fetched result
          appended_data = name, macaddress, ip, cpucount, disks, ram, ostype, osversion
          new_list.append(appended_data)
      return new_list
    except Exception as e:
      print ("Error: unable to fetch data")
      print("Exception:", e)
    # disconnect from server
    db.close()


def screen_output(datalist):
    """Function displays list to screen"""
    print()
    header = f"{'NAME':<10} {'MAC':<20} {'IP':<15} {'CPU_COUNT':<10} {'DISKS':<10} {'RAM':<10} {'OSTYPE':<15} {'OSVERSION':<15}"
    print(header)
    print('-' * len(header))
    # Loop through list displaying content to screen
    for items in datalist:
        name = items[0]
        mac = items[1]
        ip = items[2]
        cpu = items[3]
        disks = items[4]
        ram = items[5]
        ostype = items[6]
        osversion = items[7]
        row = f"{name:<10} {mac:<20} {ip:<15} {cpu:<10} {disks:<10} {ram:<10} {ostype:<15} {osversion:<15}"
        print(row)


def csv_output(datalist):
    """Function accepts list to write to csv file"""
    filename = 'database2.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['NAME', 'MAC', 'IP', 'CPU_COUNT', 'DISKS', 'RAM', 'OSTYPE', 'OSVERSION']
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(fieldnames)
        for row in datalist:
          name = row[0]
          macaddress = row[1]
          ip = row[2]
          cpucount = row[3]
          disks = row[4]
          ram = row[5]
          ostype = row[6]
          osversion = row[7]
          # Now print fetched result
          appended_data = name, macaddress, ip, cpucount, disks, ram, ostype, osversion
          csv_writer.writerow(appended_data)
    print(f'\nOutput saved in {filename}')


def json_output(datalist):
    """Function accepts list to save to json file"""
    filename = 'database2.json'
    # Convert the data to a list of dictionaries
    data_dicts = {}
    for row in datalist:
        device = {
            'NAME': row[0],
            'MAC': row[1],
            'CPU_COUNT': row[3],
            'DISKS': row[4],
            'RAM': row[5],
            'OSTYPE': row[6],
            'OSVERSION': row[7]
        }
        ip = row[2]
        data_dicts[ip] = device
    with open(filename, 'w') as jsonfile:
        # Add indent parameter for a more human-readable format
        json.dump(data_dicts, jsonfile, indent=4)
    print(f'\nOutput saved in {filename}')



# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

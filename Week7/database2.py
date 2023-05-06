#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script connects to the database and prints out the data in the rows to csv and json formatted files

# Versioning
# Scott-20230504: initial version

# Set up initial variables and imports
import sys
import pymysql
import json

DB_LOCATION = '44.205.160.194'
DB_USER = 'cmdb'
DB_NAME = 'cmdb'
DB_PASS = 'cmdbpass'
TABLE_NAME = 'devices'


# Main routine that is called when script is run
def main():
    file_output_type = argument_check()
    data_list = get_data()
    #screen_output(data_list)
    #if file_output_type == 'csv':
        #csv_output(data_list)
    #elif file_output_type == 'json':
        #json_output(data_list)
    print(data_list)

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
    # Create Array
    data_array = []
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
          data_array.append(appended_data)
      return data_array
    except:
      print ("Error: unable to fetch data")

    # disconnect from server
    db.close()


def screen_output(datalist):
    """Function displays list of dictionaries to screen"""
    print()
    header = f"{'IP':<25} {'DNS':<15}"
    print(header)
    print('-' * len(header))
    # Loop through list of dictionaries displaying content to screen
    for scan_dict in datalist:
        ip_address = scan_dict['address']
        host = scan_dict['hostname']
        row = f"{ip_address:<25} {host:<15}"
        print(row)


def csv_output(datalist):
    """Function writes list of dictionaries to csv file"""
    filename = 'nmap3a.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP', 'DNS']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        # Loop through dictionary writing to csv file
        for scan_dict in datalist:
            row_dict = {'IP': scan_dict['address'], 'DNS': scan_dict['hostname']}
            csv_writer.writerow(row_dict)
    print(f'\nOutput saved in {filename}')


def json_output(datalist):
    filename = 'nmap3a.json'
    with open(filename, 'w') as jsonfile:
        json.dump(datalist, jsonfile)
    print(f'\nOutput saved in {filename}')


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

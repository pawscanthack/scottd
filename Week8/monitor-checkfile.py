#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
#  Script reads the data of file hashes in the database, then checks them against newly calculated hashs of the files on disk.  It will then print out a csv file (filecheck.csv) with the results

# Versioning
# Scott-20230513: initial version

# Set up initial variables and imports
import pymysql
import sys
import hashlib
import os
from datetime import datetime
import csv

DB_LOCATION = '44.205.160.194'
DB_USER = 'cmdb'
DB_NAME = 'cmdb'
DB_PASS = 'cmdbpass'
TABLE_NAME = 'file_hashes'


# Main routine that is called when script is run
def main():
    db_list = get_data()
    results_list = check_hashes(db_list)
    screen_output(results_list)
    write_to_csv(results_list)


# Subroutines
def get_data():
    """Function connects to database and returns data as a list"""
    # Create list
    new_list = []
    # Open database connection
    connection = create_db_connection(DB_LOCATION, DB_USER, DB_PASS, DB_NAME)
    # prepare a cursor object using cursor() method
    cursor = connection.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = f"SELECT * FROM {TABLE_NAME}"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        print("\nMySQL Database connection successful")
        return results
    except Exception as e:
        print ("Error: unable to fetch data")
        print("Exception:", e)
    # disconnect from server
    connection.close()


def check_hashes(dblist):
    result = []
    for list in dblist:
        changed = compare_hash(list)
        appended_info = list[1], list[2], list[0], changed[0], changed[1]
        result.append(appended_info)
    return result


def compare_hash(target_list):
    previous_hash = target_list[2]
    #FIX: Add error handling
    current_hash = calculate_md5(target_list[1])
    if current_hash != previous_hash:
        return current_hash, "changed"
    elif current_hash == previous_hash:
        return current_hash, "unchanged"
    else:
        return current_hash, "Error"


def calculate_md5(file_name):
    hash_md5 = hashlib.md5()
    #FIX: Add error handling
    with open(file_name, "rb") as file:
        # Read the file in chunks to handle large files efficiently
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def create_db_connection(host_name, user_name, user_password, db_name):
    """Function creates and returns DB connection"""
    connection = None
    try:
        connection = pymysql.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Exception as e:
        print(f"Error: '{e}'")
    return connection


def screen_output(list_data):
    """Function displays dictionary to screen"""
    print()
    header = f"{'PATH':<50} {'DB_HASH':<35} {'HASH_DATE':<30} {'CURRENT_HASH':<35} {'STATUS':<20}"
    print(header)
    print('-' * len(header))
    for list in list_data:
        # Assign list values to variable
        file_path = list[0]
        db_hash = list[1]
        hash_date = list[2]
        current_hash = list[3]
        status = list[4]
        row = f"{file_path:<50} {db_hash:<35} {hash_date:<30} {current_hash:<35} {status:<20}"
        print(row)
    print()


def write_to_csv(datalist):
    """Function accepts list to write to csv file"""
    filename = 'filecheck.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['PATH','DB_HASH','HASH_DATE','CURRENT_HASH','STATUS']
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(fieldnames)
        for list in datalist:
            # Assign list values to variable
            file_path = list[0]
            db_hash = list[1]
            hash_date = list[2]
            current_hash = list[3]
            status = list[4]
            appended_data = file_path, db_hash, hash_date, current_hash, status
            csv_writer.writerow(appended_data)
    print(f'\nOutput saved in {filename}')


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

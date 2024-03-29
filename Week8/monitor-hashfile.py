#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
#  Script takes argument on the command line for a full file path such as /etc/hosts, creates a MD5 hash of the file and add the timestamp in zulu time, the file path, and add the hash to a database table in the mysql server.

# Versioning
# Scott-20230513: initial version

# Set up initial variables and imports
import pymysql
import sys
import hashlib
import os
from datetime import datetime

DB_LOCATION = '44.205.160.194'
DB_USER = 'cmdb'
DB_NAME = 'cmdb'
DB_PASS = 'cmdbpass'
TABLE_NAME = 'file_hashes'


# Main routine that is called when script is run
def main():
    check_argument()
    hash_list = build_list(sys.argv[1])
    screen_output(hash_list)
    write_to_db(hash_list)


# Subroutines
def check_argument():
    """Function checks for presence of argument and gives usage if argument is missing"""
    if  not len(sys.argv) == 2:
        print("Usage: monitor-hashfile.py [file]")
        sys.exit(1)
    else:
        return 


def build_list(file_to_hash):
    """Function returns time, path, and hash for target file"""
    file_hash = calculate_md5(file_to_hash)
    path = os.path.abspath(file_to_hash)
    timestamp = datetime.now().isoformat()
    list = [timestamp,path,file_hash]
    return list


def calculate_md5(file_name):
    """Function returns md5 hash for file"""
    hash_md5 = hashlib.md5()
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
    """Function displays list to screen"""
    print()
    header = f"{'TIMESTAMP':<35} {'PATH':<40} {'HASH':<30}"
    print(header)
    print('-' * len(header))
    # Assign list values to variable
    timestamp = list_data[0]
    file_path = list_data[1]
    hash = list_data[2]
    row = f"{timestamp:<35} {file_path:<40} {hash:<30}"
    print(row)
    print()


def write_to_db(list_data):
    """Function inserts data into database from list"""
    timestamp = list_data[0]
    path = list_data[1]
    hash = list_data[2]
    connection = create_db_connection(DB_LOCATION, DB_USER, DB_PASS, DB_NAME)
    cursor = connection.cursor()

    sql = f"INSERT INTO {TABLE_NAME}(timestamp, path, hash) \
    VALUES ('%s', '%s', '%s')" % (timestamp, path, hash)
    try:
        cursor.execute(sql)
        connection.commit()
        print("MySQL write to database successful")
    except Exception as Error:
        connection.rollback
        print(f"MySQL Database update unsuccessful: {Error}")
    connection.close()
    return


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

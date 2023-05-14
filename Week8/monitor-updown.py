#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script will check if the servers in the file servers.csv are up or down every 10 seconds and write the results to updown.csv
# Enter 'kill' to terminate program

# Scott-20230514: initial version

# Set up initial variables and imports
import csv
import time
from pinglib import pingthis
from datetime import datetime
import threading

TARGET_FILE = "servers.csv"

# Global variable to track the monitoring state
monitoring = True

# Main routine that is called when script is run
def main():
    file_check(TARGET_FILE)
    target_list = read_csv(TARGET_FILE)
    monitor(target_list)
    print("Have a great day!")

# Subroutines
def file_check(file_name):
    """Function checks if user input is a valid filename"""
    try:
        with open(file_name, 'r') as file:
            return 1
    except FileNotFoundError:
        print(f"{TARGET_FILE} not found.")
        exit(1)
    
def read_csv(file):
    """Function reads csv file to list"""
    with open(file, 'r') as file:
        csv_reader = csv.reader(file)
        targetlist = [item for sublist in csv_reader for item in sublist]
        return targetlist

def monitor(targetlist):
    """Function performs monitoring and data output to screen and csv"""
    while monitoring:
        print("\nMonitoring in progress, enter 'kill' to terminate program")
        print()
        header = f"{'TIMESTAMP':<30} {'IP':<20} {'TEST':<10} {'STATUS':10}"
        fields = ['timestamp', 'IP', 'test', 'status']
        print(header)
        with open('updown.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow(fields)
            for target in targetlist:
                ping_result = pingthis(target)
                formatted_result = format_result(ping_result)
                timestamp = formatted_result[0]
                ip = formatted_result[1]
                test = formatted_result[2]
                status = formatted_result[3]
                screen_row = f"{timestamp:<30} {ip:<20} {test:<10} {status:10}"
                print(screen_row)
                csv_row = timestamp, ip, test, status
                write.writerow(csv_row)
            print("Waiting...")
            time.sleep(10)

def format_result(list):
    """Function formats results into specified output"""
    newlist = []
    timestamp = datetime.now().isoformat()
    ip = list[0]
    type = "updown"
    if isinstance(list[1], float):
        status = "up"
    elif isinstance(list[1], str):
        status = "down"
    else:
        status = "WTF?"

    newlist = timestamp, ip, type, status
    return newlist

def input_thread():
    """Function waits for user input to exit program using threading"""
    global monitoring
    while True:
        if input().lower() == "kill":
            print("Terminating program...")
            monitoring = False
            break

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main_thread = threading.Thread(name="main_program", target=main)
    input_thread = threading.Thread(name="input_thread", target=input_thread)

    main_thread.start()
    input_thread.start()

    main_thread.join()
    input_thread.join()

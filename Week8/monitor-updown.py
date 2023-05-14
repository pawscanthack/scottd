#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script will check if the servers in the file servers.csv are up or down every 10 seconds and write the results to updown.csv

# Scott-20230514: initial version

# Set up initial variables and imports
import csv
import time
from pinglib import pingthis
import threading

TARGET_FILE = "servers.csv"

# Global variable to track the monitoring state
monitoring = True

# Main routine that is called when script is run
def main():
    print("MAIN PROGRAM")
    file_check(TARGET_FILE)
    target_list = read_csv(TARGET_FILE)
    print(target_list)
    monitor(target_list)
    print("EXCITING!")

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
    while monitoring:
        for target in targetlist:
            ping_result = pingthis(target)
            print(ping_result)
        time.sleep(10)

def input_thread():
    global monitoring
    while True:
        if input().lower() == "kill":
            print("Terminating program")
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

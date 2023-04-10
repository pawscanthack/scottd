#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""

# Script which inputs a birthdate as mm-dd-yyyy and a number of days such as 20000, then prints out the date that a person with the birthday will reach that number of days

# Scott-20230410: initial version

# Set up initial variables and imports
import sys
import datetime

# Main routine that is called when script is run
def main():
    """Checks for presence of arguments"""
    # Check that two arguments were provided: birthdate and number of days
    if len(sys.argv) != 3:
        print("Usage: dates [mm-dd-yyyy] [days]")
        sys.exit(1)

    try:
        # Parse the birthdate argument into a datetime object
        date_obj = datetime.datetime.strptime(sys.argv[1],"%m-%d-%Y")
    except Exception as ge:
        # If the birthdate argument is invalid, print an error message and exit with status 1
        print("Error:", ge)
        sys.exit(1)

    try:
        # Parse the number of days argument into an integer
        int_days = int(sys.argv[2])
    except Exception as ge:
        # If the number of days argument is invalid, print an error message and exit with status 2
        print("Error:", ge)
        sys.exit(2)

    # Calculate the future date and print it
    print(calc_future_date(date_obj, int_days))

def calc_future_date(start_date, interval_days):
    """
    Function accepts a datetime object and an integer representing the number of days to add,
    then returns the future date as a string in the format mm-dd-yyyy.
    """
    # Calculate the future date by adding the number of days to the start date
    delta = datetime.timedelta(days=interval_days)
    future = start_date + delta

    # Format the future date as a string in the desired format
    return future.strftime("%m-%d-%Y") 

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script which inputs are in a birthdate as mm-dd-yyyy and a number of days such as 20000, then prints out the date that a person with the birthday will reach that number of days

# Scott-20230410: initial version


# Set up initial variables and imports
import sys
import datetime

# Main routine that is called when script is run
def main():
    """Checks for presence of arguments"""
    if len(sys.argv) != 3:
        print("Usage: dates [mm-dd-yyyy] [days]")
        sys.exit(1)
    
    try:
        date_obj = datetime.datetime.strptime(sys.argv[1],"%m-%d-%Y")

    except Exception as ge:
        print("Error:", ge)
        sys.exit(1)

    try:
        int_days = int(sys.argv[2])

    except Exception as ge:
        print("Error:", ge)
        sys.exit(2)

    print(calc_future_date(date_obj, int_days))

def calc_future_date(start_date, interval_days):
    """
    Function accepts datetime object and integer then returns future date
    """
    delta = datetime.timedelta(days=interval_days)
    future = start_date + delta
    return future.strftime("%m-%d-%Y")

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

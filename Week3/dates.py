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
SITES = ['bhs','ah','lms']
MAIL_SERVER = 'smtp.google.com'
""" < 
Put any global or initial variables here. This is the only place where folks
should make quick changes to the script such as using a different mail server
account.  Change/remove the example lines above as needed 
> """

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
        int_days = sys.argv[2]

    except Exception as ge:
        print("Error:", ge)
        sys.exit(2)

    print(date_obj, ":", int_days)

    


  # Get the messages and process them
""" <
The functions code goes here. Use comments in the code to explain what
large blocks of it do or for something you may not remember how it works
> """


# Subroutines
""" <
The subroutines called by the main function are listed here
> """



# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""

# Script that reads arguments, all positive numbers, on the command line and finds their average to two decimal places

# Versioning
# Scott-20230430: initial version

# Set up initial variables and imports
import sys

# Main routine that is called when script is run
def main():
    # Check for arguments, if absent print usage message
    if len(sys.argv) < 2:
        print("Usage: avgn.py [number1] [number2] ... [numberN]")
        sys.exit(1)

    # Check for valid arguments and assign to numbers list, if not raise exception and print error message
    try:
        numbers = []
        for arg in sys.argv[1:]:
            try:
                num = float(arg)  # Convert argument to float
                if num < 0:  # Check if argument is negative
                    raise ValueError("All arguments must be positive numbers")
                numbers.append(num)  # Add argument to list of valid numbers
            except ValueError:
                print(f"Error: {arg} is not a valid number")  # Print error message for invalid argument
                sys.exit(1)  # Exit program with error code

        # Call avg function with valid numbers and print result
        average = avg(*numbers)
        numbers_str = ", ".join(str(num) for num in numbers)  # Convert list of numbers to comma-separated string
        print(f"Average of {numbers_str} is {average:.2f}")  # Print formatted average

    except ValueError as ve:
        print("Error:", ve)  # Print error message for invalid argument or negative argument
        sys.tracebacklimit = 0 # Suppress traceback
        sys.exit(1)  # Exit program with error code



# Subroutines
def avg(*args):
    """Function to calculate the average and round results to two places"""
    try:
        # Check for arguments
        if len(args) < 1:
            raise ValueError("At least one number must be provided")

        # Validate argument data type and sign
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError("All arguments must be numbers")
            if num < 0:
                raise ValueError("All arguments must be positive numbers")

        # Calculate average
        total = sum(args)
        average = total / len(args)
        rounded_average = round(average, 2)
        return rounded_average

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")  # Print error message for invalid or negative argument



# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

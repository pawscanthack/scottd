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
        numbers = [float(arg) for arg in sys.argv[1:]]
        if any(num < 0 for num in numbers):
            raise ValueError("All arguments must be positive numbers")

        
        #Call avg function
        average = avg(*numbers)
        numbers_str = ", ".join(str(num) for num in numbers)
        print(f"Average of {numbers_str} is {average:.2f}")

    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)

# Subroutines
def avg(*args):
    """Function to calculate the average and round results to two places"""
    try:
        # Verify argument data type and value
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError("All arguments must be numbers")
            if num < 0:
                raise ValueError("All arguments must be positive numbers")

        # Check for arguments
        if len(args) < 1:
            raise ValueError("At least one number must be provided")

        # Calculate average
        total = sum(args)
        average = total / len(args)
        rounded_average = round(average, 2)
        return rounded_average

    except (TypeError, ValueError) as e:
        print("Error:", e)
        sys.exit(1)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
    main()

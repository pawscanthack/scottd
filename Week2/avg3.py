#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script that reads in three arguments, all positive numbers, on the command line and finds their average to two decimal places

# Versioning
# Scott-20230406: initial version

# Set up initial variables and imports
import sys

# Main routine that is called when script is run
def main():
    """Checks for presence of arguments"""
    if len(sys.argv) != 4:
        print("Usage: avg3 [number1] [number2] [number3]")
        sys.exit(1)

    try:
        num1, num2, num3 = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])

        if num1 <= 0 or num2 <= 0 or num3 <= 0:
            raise ValueError("All arguments must be positive numbers")

        average = (num1 + num2 + num3) / 3
        print(f"Average of {num1}, {num2}, and {num3} is {average:.2f}")

    except ValueError as ve:
        print("Error:", ve)
        sys.exit(1)

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

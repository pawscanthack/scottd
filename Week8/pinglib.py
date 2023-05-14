#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# reads in a single IP or DNS name on the command line, calls the function to ping it, and then displays the result
# also callable via the pingthis() function which returns a list of the results

# Versioning
# Scott-20230415: initial version

# Set up initial variables and imports
import subprocess
import sys

# Main routine that is called when script is run
def main():
    """reads in a single IP or DNS name on the command line, calls the function to ping it, and then displays the result"""
    # Get the IP or DNS name from the command line
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        # Call the ping function
        result = pingthis(ip)
        if result[1] == "Not Found":
            print(f"Could not ping {result[0]}")
            sys.exit(1)
        else:
            # print(f"ping to {result[1]} took {result[0]} ms")
            print(f"IP, TimeToPing (ms)\n{result[0]}, {result[1]}")
    else:
        print("Usage: pinglib.py <ip or dns name>")
        # pingthis("10.2.3.3")
        sys.exit(1)

# Subroutines

def pingthis(ip):
    """Pings the IP or DNS name passed to it"""
    # Call the ping command
    ping = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    # Check the return code
    if ping.returncode == 0:
        ping_decoded = ping.stdout.decode()
        return process_data(ping_decoded)
    else:
        return [ip, "Not Found"]  
    
def process_data(ping_data):
    """Processes the output from the ping command"""
    # Split the output into lines
    lines = ping_data.splitlines()

    # Find the line that contains the PING target (i.e., starts with "PING")
    target_line = next(line for line in lines if line.startswith("PING"))

    # Find the line that contains the ping response (i.e., starts with "64 bytes from")
    time_line = next(line for line in lines if line.startswith("64 bytes from"))

    # Extract the time value and PING target from the ping response lines
    ping_target = target_line.split('(')[1].split(')')[0]
    time_string = time_line.split()[-2]
    time_value = time_string.split('=')[1]

    # Return the time value and PING target as a list
    return [ping_target, float(time_value)]
    


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

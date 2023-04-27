#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script that does a syn scan only of DEFAULT_TARGETS(152.157.64.0/24 and 152.157.65.0/24) and 
# Creates a CSV of the IPs and open ports

# Versioning
# Scott-20230427: initial version

# Set up initial variables and imports
import nmap3
DEFAULT_TARGET_LIST =['152.157.64.0/24', '152.157.65.0/24']


# Main routine that is called when script is run
def main():
  scan_result = scan_target_list(DEFAULT_TARGET_LIST)
  #file_output(scan_result)
  #screen_output(scan_result)
  print(scan_result)



# Subroutines
def scan_target_list(list):
    result = {}
    for target in list:
        nmap = nmap3.Nmap()
        result.update(nmap)
    return result


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

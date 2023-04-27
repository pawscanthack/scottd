#!/usr/bin/python3
"""
Scott Davis
SEC444
Bellevue College
Spring 2023
"""
# Script that does a syn scan only of DEFAULT_TARGETS(152.157.64.0/24 and 152.157.65.0/24)
# Creates a CSV of the IPs and open ports

# Versioning
# Scott-20230427: initial version

# Set up initial variables and imports
import nmap3
DEFAULT_TARGET_LIST =['152.157.64.0/24', '152.157.65.0/24']
#DEFAULT_TARGET_LIST =['scanme.nmap.org']


# Main routine that is called when script is run
def main():
    scan_result = scan_target_list(DEFAULT_TARGET_LIST)
    filtered_result = filter_scan_result(scan_result)
    #file_output(scan_result)
    #screen_output(scan_result)
    #print(filtered_results)



# Subroutines
def scan_target_list(list):
    result = {}
    nmap = nmap3.NmapScanTechniques()
    for target in list:
        scan_data = nmap.nmap_syn_scan(target)  # Perform syn scan on the target
        result[target] = scan_data  # Update the result dictionary with the scan data
    return result

def filter_scan_result(dict):
    for main_key, nested_dict in dict.items():
        print(main_key)
        for nested_dict, nested_value in nested_dict.items():
            print(nested_dict)
            print(nested_value)


# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

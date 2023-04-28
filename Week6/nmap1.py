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
    print(filtered_result)



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
        return_dict = {}
        ip_address_key = list(nested_dict.keys())[0]
        # Iterate through the 'ports' list
        print(ip_address_key)
        for ip_address_key, ip_info in nested_dict.items():
            if 'ports' in ip_info:
                for port_info in ip_info['ports']:
                    # Check if the 'state' is 'open'
                    if port_info['state'] == 'open':
                        print(f"Port {port_info['portid']} is open.")
                        port = port_info['portid']
                        if ip_address_key not in return_dict:
                            return_dict.update({ip_address_key: port})
                        if ip_address_key in return_dict:
                            # Apend new open port to dictionary value for ip_address_key
                            return_dict[ip_address_key] += ' ' + port
                    else:
                        print(f"Port {port_info['portid']} is not open (state: {port_info['state']}).")
    return return_dict

# Run main() if script called directly, else use as a library to be imported
if __name__ == "__main__":
        main()

#!/usr/bin/python3
# Fix each section function to complete this homework then upload this file.
# I will run the file and verify the answers

# Globals
RESULTS = {'152.157.64.5': {'osmatch': {}, 'ports': [{'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'http', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '113', 'state': 'closed', 'reason': 'reset', 'reason_ttl': '51', 'service': {'name': 'ident', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '443', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'https', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}], 'hostname': [], 'macaddress': None, 'state': {'state': 'up', 'reason': 'syn-ack', 'reason_ttl': '49'}}, 'runtime': {'time': '1680459977', 'timestr': 'Sun Apr  2 11:26:17 2023', 'elapsed': '15.08', 'summary': 'Nmap done at Sun Apr  2 11:26:17 2023; 1 IP address (1 host up) scanned in 15.08 seconds', 'exit': 'success'}, 'stats': {'scanner': 'nmap', 'args': '/usr/bin/nmap -v -oX - -sS 152.157.64.5', 'start': '1680459961', 'startstr': 'Sun Apr  2 11:26:01 2023', 'version': '7.80', 'xmloutputversion': '1.04'}, 'task_results': [{'task': 'Ping Scan', 'time': '1680459962', 'extrainfo': '1 total hosts'}, {'task': 'Parallel DNS resolution of 1 host.', 'time': '1680459972'}, {'task': 'SYN Stealth Scan', 'time': '1680459976', 'extrainfo': '1000 total ports'}]}

# Functions
def main():
    "Loop through all the sections"
    for i in range(1,9):
        cmd = 'section'+str(i)+'()'
        eval(cmd)
        print('\n')

def section1():
    print('### Section 1')
    print("### Should print '3'")
    a1 = 1
    a2 = 5
    if a1 > a2:
        print('3')
    else:
        print('4')

def section2():
	print('### Section 2')
	print("### Should print 'cat'")
	a2 = ['cat', 'dog', 'bird']
	print(a2[1])

def section3():
    print('### Section 3')
    print("### Should print 'Cutie my cat loves her cat door'")
    mystring = "Cutie my cat loves her cut door"
    mystring = mystring.replace('u','a')
    print(mystring)

    
def section4():
    print('### Section 4')
    print('### Should print (may be in a different order):')
    print('###   Timber is my dog')
    print('###   Mido is my cat')
    print('###   Whiskers is my mouse')
    print('###   Tweety is my bird')
    mypets = {'Mido':'cat', 'dog':'Timber', 'mouse':'Whiskers'}
    for k,v in mypets.items():
        print(k + ' is my ' + v)

def section5():
    print('### Section 5')
    print('### Should print 120')
    def fact(x):
        if x == 1:
            return 0
        else:
            return(x + fact(x - 1))
    res = fact(5)
    print(res)

def section6():
    print('### Section 6')
    print("### Should print 'Ports scanned: 1000 total ports'")
    print('Ports scanned: '+ RESULTS['stats']['scanner'])


def section7():
    print('### Section 7')
    print("### Should print 'Elapsed time: 15.08'")
    print('Elapsed time: '+ RESULTS['task_results'][0]['task'])

def section8():
    print('### Section 8')
    print("### Should print the following")
    print('###   Service ssh on port 22')
    print('###   Service http on port 80')
    print('###   Service https on port 443')
    for ports in RESULTS['152.157.64.5']['ports']:
        print('Service ' + ports['protocol'] + ' on port ' + ports['state'])


# Run main() if script called directly
if __name__ == "__main__":
        main()


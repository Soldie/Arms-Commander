#!/usr/bin/env python
# coding=UTF-8
import os
import socket
import operator
from termcolor import colored
import sys
import toolkits
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen


os.chdir('/root/ArmsCommander')


#The first line allows this script to be executable

# ArmsCommander - "Revolutionizing Cyber-Terrorism"

# Black chant mirrors the song of the stars
# Open the abyss dreamt from afar
# Abominations drawn to our dimension
# Feed black desires, aid human ascension
#
# Black chanting grows
# From caverns below
# Echo through time
# Reveal the sign

os.system('cat /root/ArmsCommander/banners/ACBanner.txt')
logfile_directory = '/root/ArmsCommander/logs'
print colored("""
                    Black chanting grows
                    From caverns below
                    Echo through time
                    Reveal the sign

""",'red')

def dorah_explorah():
    os.chdir("/root/ArmsCommander/recon")
    os.system('cat /root/ArmsCommander/banners/dorah_explorah.txt')
    cmd_String = "python /root/ArmsCommander/recon/dorah_explorah.py"
    os.system(cmd_String)
def search_logs(search_term, logfile_directory):
    cmd_String = 'find %s -iname "*%s*"' % (logfile_directory, search_term)
    os.system(cmd_String)
    one_recon_and_vuln_scan()
def MT_host_recon():
    os.system('python /root/ArmsCommander/recon/multi_tool_recon.py')
    return

def CornHarvester():
    os.system('python /root/ArmsCommander/recon/CornHarvester_Menu.py')
    return

def NMap_Auto():
    os.system('python /root/ArmsCommander/recon/nmap.py')
    return

def SQLMap():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/proxychainsTest.py; exec bash\"'")
    os.system('python /root/ArmsCommander/recon/SQLMapCustom.py')
    return

def OWASP_zaproxy():
    os.system("gnome-terminal -e 'bash -c \"zaproxy; exec bash\"'")
    main()
    return

def burpsuite():
    os.system("gnome-terminal -e 'bash -c \"burpsuite; exec bash\"'")
    main()
    return

def output_data():
    Menu_Header = colored('OUTPUT, BACKUP, IMPORT YOUR LOGFILES', 'cyan', attrs=['bold'])
    print Menu_Header

    print 'For further reference, all data was saved in your /root/ArmsCommander/logs/ directory if you wanted to access them or back it up manually'
    opt_List = [
        '\n\t#0. Return to Previous Menu',
        '#1. Output all MULTI-TOOL SCAN DATA',
        '#2. Output all CORNHARVESTER DATA',
        '#3. Output all NMAP DATA',
        '#4. Make a logfile backup of the data using RSYNC (unintrusive, wont copy over files)',
        '#5. IMPORT logfile backups from a specified directory'
    ]

    print("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        os.system('cat /root/ArmsCommander/logs/multi_tool_recon/*')
        output_data()
    elif opt_Choice == "2":
        os.system('clear')
        os.system('cat /root/ArmsCommander/logs/CornHarvester/*')
        output_data()
    elif opt_Choice == "3":
        os.system('clear')
        os.system('cat /root/ArmsCommander/logs/nmap/*')
        output_data()
    elif opt_Choice == "0":
        os.system('clear')
        one_recon_and_vuln_scan()
    elif opt_Choice == "4":
        os.system('clear')
        cmd_String = "rsync -v -r /root/ArmsCommander/logs /root/Documents/ArmsCommander_logs_backup"
        os.system(cmd_String)
        user_String = 'All files backed up in folder: /root/Documents/ArmsCommander_logs_backup'
        print colored(user_String,'red','on_white')
        output_data()
    elif opt_Choice == "5":
        import_directory = str(raw_input("Enter the full directory path where the to-be-imported files are located: "))
        import_path = import_directory + '/*'
        cmd_String = "rsync -v -r %s /root/ArmsCommander/logs" % import_path
        os.system(cmd_String)
        print colored('All log files imported to /root/ArmsCommander/logs','red','on_white')
        output_data()
    else:
        print colored('You have entered a invalid option','red')
        output_data()

    return

def dmitry():
    os.system('python /root/ArmsCommander/recon/dmitry_menu.py')
    one_recon_and_vuln_scan()
    return
def one_recon_and_vuln_scan():
    Menu_Header = colored('RECONNAISSANCE AND ENUMERATION', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Multi-Tool Single Host Recon, use Dig, NSLookup, fierce, and theharvester against a single target',
        '#2. CornHarvester, mass-harvest emails for phishing/Spear-Phishing',
        '#3. DMITRY, DeepMagic Information Gathering Tool, with my added wordlist-automation enhancements',
        '#4. NMap Scans (preset for maximum information discovery), starts with FIN scan, then XMAS scan, and finally a comprehensive scan',
        '#5. Run SQLMap (Automatically set to route traffic through Tor)',
        '#6. OWASP Zaproxy (Alternative vulnerability scanner, much faster than SQLMap)',
        '#7. BurpSuite',
        '#8. OUTPUT/BACKUP ALL DATA collected from Multi-Tool, CornHarvester, and NMap',
        '#9. Dorah, the Explorah: I wanna Explorah your booty! A NMap EZ-Mode Script Menu, 568 Scripts'
        ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        MT_host_recon()
    elif opt_Choice == "2":
        os.system('clear')
        CornHarvester()
    elif opt_Choice == "3":
        os.system('clear')
        dmitry()
    elif opt_Choice == "4":
        os.system('clear')
        NMap_Auto()

        # NMap_Custom()
    elif opt_Choice == "5":
        os.system('clear')
        SQLMap()

        # SQLMap()
    elif opt_Choice == "6":
        os.system('clear')
        OWASP_zaproxy()

    elif opt_Choice == "7":
        os.system('clear')
        burpsuite()

    elif opt_Choice == "8":
        os.system('clear')
        output_data()

    elif opt_Choice == "9":
        os.system('clear')
        dorah_explorah()
        one_recon_and_vuln_scan()

    else:
        print colored('You have entered a invalid option','red')
        one_recon_and_vuln_scan()
    return

def tor_and_proxychains():
# /root/ArmsCommander/networkdefenses/proxychainsTest.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/proxychainsTest.py; exec bash\"'")
    main()
    return

def network_monitor_tools():
    #Snort
    print colored('Launching Intrusion Detection System','red','on_white')
    os.system("gnome-terminal -e 'bash -c \"sudo snort -q -A console -c /etc/snort/snort.conf; exec bash\"'")

    #p0f
    print colored('Starting p0f, passive OS fingerprinter','red','on_white')
    os.system("gnome-terminal -e 'bash -c \"sudo p0f; exec bash\"'")
    #viewActiveConnections
    print colored('Listing Real Time Active Connections','red','on_white')
    os.system("gnome-terminal -e 'bash -c \"sudo watch -b -c ss -tp; exec bash\"'")
    print colored('Starting Fail-2-Ban Service','yellow',attrs=['bold'])
    os.system("gnome-terminal -e 'bash -c \"service fail2ban restart; exec bash\"'")
    main()

    return

def cover_tracks():
    print 'Clearing bash history'
    os.system('rm -rf /root/.bash_history')
    print 'Clearing thumbnails'
    os.system('rm -rf /root/.cache/thumbnails')

    print colored('Both your bash shell history and your thumbnails cache has been WIPED. Warning, the data can still be recovered, you must overwrite the disk with zeroes using the Kali Installer to fully eliminate forensic recovery','red','on_white')
    print"""
    Furthermore, using this does not completely eliminate the need to...

    1. Delete your trash
    2. Clean out your auth logs

    This only prevents LE from finding the most incriminating information in five minutes
    """
    print colored('Retain a lawyer before you resort to doing anything bad','red','on_white')
    main()
    return

def TCPKill():
# /root/ArmsCommander/networkdefenses/TCPKill.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/TCPKill.py; exec bash\"'")


    return

def NGrep():
# /root/ArmsCommander/networkdefenses/NGrepCustom.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/NGrepCustom.py; exec bash\"'")

    return

def macchanger():
# /root/ArmsCommander/networkdefenses/macChanger.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/macChanger.py; exec bash\"'")

    return

def fuser():
    Menu_Header = colored('FUSER', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
                '\n\t#1. LOOKUP all process IDs of a port and protocol',
                '#2. Terminate all connections of a port/protocol'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "1":
        fuser_port = str(raw_input("Enter a PORT: "))
        fuser_protocol = str(raw_input("Enter a PROTOCOL(tcp/udp): "))
        fuser_cmd_string = "fuser %s/%s" % (fuser_port, fuser_protocol)
        os.system(fuser_cmd_string)
    elif opt_Choice == "2":
        fuser_port = str(raw_input("Enter a PORT: "))
        fuser_protocol = str(raw_input("Enter a PROTOCOL(tcp/udp): "))
        fuser_cmd_string = "fuser -k %s/%s" % (fuser_port, fuser_protocol)
        os.system(fuser_cmd_string)
    elif opt_Choice == "0":
        main()
    else:
        print colored('You have entered a invalid option','red','on_white')
    main()
    return

def IDS_Flooder():
# /root/ArmsCommander/networkdefenses/IDS_flood.py
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/IDS_flood.py; exec bash\"'")

    return

def fail2ban():
    os.system('service fail2ban restart')
    os.system('service fail2ban status')
    main()
    return

def jkd_poc():
    # remember to import toolkits
    print toolkits.yellow("DO NOT CLOSE THIS WINDOW! \nLet this process run when their scans hit you")
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/networkdefenses/JKD_poc.py; exec bash\"'")
    return
def two_net_defense_traffic_monitor():
    Menu_Header = colored('NETWORK DEFENSE', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#1. Tor + Proxychains, conceal your outbound traffic',
        '#2. Network Monitoring Tools, p0f, Snort, and view active network connections',
        '#3. Cover your tracks, clear your bash history and wipe your thumbnails cache',
        '#4. TCP Kill a connection by host, IP, or port',
        '#5. NGrep or "Network Grep", investigate a suspicious connection',
        '#6. MacChanger, change your network card MAC address temporarily',
        '#7. Fuser, identify and kill processes within a port range',
        '#8. IDS Flooder, overwhelm a Intrusion Detection System with false-flag DDoS attacks to draw attention away from your actual activity',
        '#9. FAIL-2-BAN, automatic banning daemon for SSH. Absolutely essential for remote AWS servers that are subjected to constant SSH brute-force attacks',
        '#10. VIEW AUTH LOG, view your authentication log and make a backup of it.',
        '#11. ***NEW***, JKD: Bluce-Ree Edition, auto-counterattack aggressive NMAP scans using a Metasploit Server Design Flaw'
    ]
    print ("\n\t".join(opt_List))

    print toolkits.green('\t' + opt_List[11])
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        print colored('[+] Starting Tor + Proxychains','green', attrs=['bold'])
        tor_and_proxychains()
        # MT_host_recon()
    elif opt_Choice == "2":
        os.system('clear')
        print colored('[+] Starting Monitoring Tools','green', attrs=['bold'])
        network_monitor_tools()
        # CornHarvester()
    elif opt_Choice == "3":
        os.system('clear')
        print colored('[+] Starting Cover Your Tracks','green', attrs=['bold'])
        cover_tracks()
        # NMap_Auto()
    elif opt_Choice == "4":
        os.system('clear')
        print colored('[+] Starting TCP Kill','green', attrs=['bold'])
        TCPKill()
        # NMap_Custom()
    elif opt_Choice == "5":
        os.system('clear')
        print colored('[+] Starting Network Grep','green', attrs=['bold'])
        NGrep()
        # SQLMap()
    elif opt_Choice == "6":
        os.system('clear')
        print colored('[+] Starting Mac Changer Interactive Menu','green', attrs=['bold'])
        macchanger()
        # OWASP_zaproxy()
    elif opt_Choice == "7":
        os.system('clear')
        print colored('[+] Starting Fuser','green', attrs=['bold'])
        fuser()
        # burpsuite()
    elif opt_Choice == "8":
        os.system('clear')
        print colored('[+] Starting IDS Flooder Module','green', attrs=['bold'])
        IDS_Flooder()
    elif opt_Choice == "9":
        os.system('clear')
        print colored('[+] Starting fail2ban Module','green', attrs=['bold'])
        fail2ban()
    elif opt_Choice == "10":
        os.system('clear')
        print colored('[+] Copying backup of auth.log to /root/Documents','yellow',attrs=['bold'])
        os.system('cp -r /var/log/auth.log /root/Documents')
        os.system('cat /var/log/auth.log')
        main()
    elif opt_Choice == "11":
        jkd_poc()
        two_net_defense_traffic_monitor()
        return
    else:
        print colored('You have entered a invalid option','red')
        two_net_defense_traffic_monitor()

    return

def metasploit():
    os.system('python /root/ArmsCommander/remoteexploits/Metasploit.py')
    main()
    return

def armitage():
    os.system('chmod 777 /root/ArmsCommander/remoteexploits/ArmitageWithProxychains.sh')
    os.system('/root/ArmsCommander/remoteexploits/ArmitageWithProxychains.sh')
    main()
    return

def easy_peasey():
    os.system('python /root/ArmsCommander/remoteexploits/EZPZ.py')
    main()
    return

def veil_evasion():
    os.system('veil-evasion')
    main()
    return

def social_engineers_toolkit():
    os.system('setoolkit')
    main()
    return

def pupy_menu():
    os.system('python /root/ArmsCommander/remoteexploits/Pupy_Menu.py')
    main()
    return

def DPMB():
    os.system('python /root/ArmsCommander/remoteexploits/DPMB.py')
    main()
    return

def VT_Checker():
    Menu_Header = colored('VIRUS-TOTAL SAFE-CHECKER', 'cyan', attrs=['bold'])
    print Menu_Header
    os.system('cat /root/ArmsCommander/banners/disclaimer_VT_Checker.txt')

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Submit a single HASH checksum to Virus Total',
        '#2. Check a entire directory at a time (probably filled with generated malware)'
    ]
    print("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))
    if opt_Choice == "1":
        sample_file = str(raw_input("Enter the full path of the file you want to check: "))
        cmd_String = "ruby /usr/share/veil-evasion/tools/vt-notify/vt-notify.rb -s %s" % sample_file
        os.system(cmd_String)
    elif opt_Choice == "2":
        sample_directory = str(raw_input("Enter the full path of the directory that you want to check: "))
        cmd_String = "ruby /usr/share/veil-evasion/tools/vt-notify/vt-notify.rb -d %s" % sample_directory
        os.system(cmd_String)
    elif opt_Choice == "0":
        main()
    else:
        print colored('You have entered a invalid option','red')
        VT_Checker()
    main()
    return

def embed_payload_pdf():
    os.system('python /root/ArmsCommander/remoteexploits/embed_pdf_pupy.py')
    main()
    return

def stitch_menu():
    os.system('python /root/ArmsCommander/remoteexploits/Stitch_Menu.py')
    return

def payload_generators_listeners():
    Menu_Header = colored('REMOTE EXPLOITS-PAYLOAD GENERATORS AND LISTENERS/HANDLERS', 'cyan', attrs=['bold'])
    print Menu_Header

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. EASY-PEASEY, the EZ-Mode Interactive MSFVenom Payload Generation Menu',
        '#2. PUPY, the alternative Python Remote Access Trojan (RAT)',
        '#3. STITCH, another alternative Python RAT that looks like the easiest to use'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        three_remote_exploits_redesigned()
    elif opt_Choice == "1":
        os.system('clear')
        easy_peasey()
        three_remote_exploits_redesigned()
    elif opt_Choice == "2":
        os.system('clear')
        pupy_menu()
        three_remote_exploits_redesigned()
    elif opt_Choice == "3":
        os.system('clear')
        stitch_menu()
        three_remote_exploits_redesigned()
    else:
        print colored('You have entered a invalid option','red')
        payload_generators_listeners()
    return

def python_mailer(): # this entire thing needs to be scrapped and rewritten I keep getting  AttributeError: 'function' object has no attribute 'get_var_python_mailer' problems
# but python itnerpreter input seems fine.
    os.system('clear')
    os.system('python /root/ArmsCommander/remoteexploits/python_mailer_menu.py')
    main()
    return
#
# # this has to be a separate module.
#     py_mailer_save_file = '/root/ArmsCommander/remoteexploits/py_mailer_save.csv'
#
#     print colored('PYTHON HTML MASS-MAILER','cyan',attrs=['bold'])
#     remote_exploits_dir = '/root/ArmsCommander/remoteexploits'
#     opt_List = [
#         '\n\t#0. Return to Remote Exploit Toolkits Menu',
#         '#1. Start a mass-mailer attack with HTML based mail',
#         '#2. Configure Python Mailer, including editing the FROM address and name',
#         '#3. View the smtpctl queue',
#         '#4. Show the smtpctl stats (bounced, failures, timeouts, successful, etc.)',
#         '#5. Activate smtpctl monitor (in real time), refer to man page for what all the columns mean',
#         '#6. Repeat the same mass-mailer attack by using the temporary save file (requires #1 to be done first)',
#         '#INSTALL, Install Python-Mailer and the opensmtpd service'
#     ]
#
#     print ("\n\t".join(opt_List))
#     opt_Choice = str(raw_input("Enter a OPTION: "))
#
#     if opt_Choice == "1":
#         print colored('Restarting opensmtpd service','yellow',attrs=['bold'])
#         os.system('service opensmtpd restart')
#         remote_exploit_toolkits.get_var_python_mailer()
#         # # remote_exploit_toolkits.get_var_python_mailer()
#         # # subject_title = str(raw_input("Enter the SUBJECT title: "))
#         # # victim_wordlist = str(raw_input("Enter the CSV wordlist PATH of victims (NAME,ADDRESS): "))
#         # # html_file = str(raw_input("Enter HTML message PATH (*.html): "))
#         # # print colored('DEBUG: subject_title = %s victim_wordlist = %s html_file = %s','red',attrs=['bold']) % (subject_title, victim_wordlist, html_file)
#         # # remote_exploit_toolkits.write_savefile_python_mailer(subject_title, victim_wordlist, html_file)
#         # remote_exploit_toolkits.write_savefile_python_mailer(subject_title, victim_wordlist, html_file)
#         # cmd_String = "python /root/ArmsCommander/remoteexploits/python-mailer/pymailer.py -s %s %s '%s'" % (html_file, victim_wordlist, subject_title)
#         # print colored(cmd_String,'red',attrs=['bold'])
#         # os.system(cmd_String)
#         # print colored('Mail sent','green',attrs=['bold'])
#         python_mailer()
#     elif opt_Choice == "2":
#         os.system('leafpad /root/ArmsCommander/remoteexploits/python-mailer/config.py')
#         python_mailer()
#     elif opt_Choice == "3":
#         os.system('clear')
#         os.system('sudo smtpctl show queue')
#         python_mailer()
#     elif opt_Choice == "4":
#         os.system('clear')
#         os.system('sudo smtpctl show stats')
#         python_mailer()
#     elif opt_Choice == "5":
#         os.system('clear')
#         os.system('sudo smtpctl monitor')
#         python_mailer()
#     elif opt_Choice == "6":
#         os.system('clear')
#         remote_exploit_toolkits.read_savefile_python_mailer(py_mailer_save_file)
#         python_mailer()
#     elif opt_Choice == "INSTALL":
#         os.system('clear')
#         os.chdir(remote_exploits_dir)
#         os.system('git clone https://github.com/qoda/python-mailer')
#         print colored('Updating APT repo','red',attrs=['bold'])
#         os.system('sudo apt-get update')
#         print colored('Installing opensmtpd','red',attrs=['bold'])
#         os.system('sudo apt-get install opensmtpd')
#         python_mailer()
#     elif opt_Choice == "0":
#         os.system('clear')
#         remote_exploit_toolkits()
#     else:
#         print colored('You have entered a INVALID OPTION','red',attrs=['bold'])
#         python_mailer()
#     return subject_title, victim_wordlist, html_file, py_mailer_save_file
def remote_exploit_toolkits():
    Menu_Header = colored('REMOTE EXPLOITS-TOOLKITS', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. VEIL-EVASION, change the signature of a Metasploit payload to evade antivirus (the msfvenom encoder hides you from Intrusion Detection Systems ONLY)',
        '#2. METASPLOIT FRAMEWORK, this is a CUSTOM MANUAL-START SCRIPT to get past those pesky database initialization errors',
        '#3. ARMITAGE, the free version of what would later be Cobalt Strike. Still useful in pentests.',
        '#4. SOCIAL ENGINEERS TOOLKIT, comes with preloaded scripts and a easy-to-use push-button style menu for hacking techniques such as spearphishing',
        '#5. PYTHON-MAILER, Python-based mass-mailer to send HTML email with'
    ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        three_remote_exploits_redesigned()
    elif opt_Choice == "1":
        os.system('clear')
        # placeholder for specific function
        print colored('[+] Starting Veil Evasion','green')
        veil_evasion()
        three_remote_exploits_redesigned()
    elif opt_Choice == "2":
        os.system('clear')
        # placeholder for specific function
        print colored('[+] Starting Metasploit Manual-Start Mode','green')
        metasploit()
        three_remote_exploits_redesigned()
    elif opt_Choice == "3":
        os.system('clear')
        # placeholder for specific function
        print colored('[+] Starting Armitage','green')
        armitage()
        three_remote_exploits_redesigned()
    elif opt_Choice == "4":
        os.system('clear')
        # placeholder for specific function
        print colored('[+] Starting Social Engineers Toolkit','green')
        social_engineers_toolkit()
        three_remote_exploits_redesigned()
    elif opt_Choice == "5":
        os.system('clear')
        python_mailer()
        three_remote_exploits_redesigned
    else:
        print colored('You have entered a invalid option','red')
        remote_exploit_toolkits()
        # placeholder for current menu
    return

def foreplay():
    os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/remoteexploits/project_foreplay/main.py; exec bash\"'")

    return
def remote_exploits_other():
    Menu_Header = colored('REMOTE EXPLOITS-OTHER', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. DONT PATCH ME BRO, the easy-mode menu to generate inject.bin files for DuckEncoder and DuckyScript Languages on USB Rubber Duckies',
        '#2. VIRUS-TOTAL SAFE-CHECKER (VT-Notify of Veil Evasion), compare just the hash of a newly generated payload without submitting it to VT to avoid being added to antivirus databases'
    ]
    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        three_remote_exploits_redesigned()
    elif opt_Choice == "1":
        os.system('clear')
        print colored('[+] Starting Dont Patch Me Bro','green')
        # placeholder for specific function
        DPMB()
        three_remote_exploits_redesigned()
    elif opt_Choice == "2":
        os.system('clear')
        print colored('[+] Starting Virus-Total Safe-Checker','green')
        # placeholder for specific function
        VT_Checker()
        three_remote_exploits_redesigned()
    else:
        print colored('You have entered a invalid option','red')
        # placeholder for current menu
    return

def three_remote_exploits_redesigned(): # Tentative project to reduce bloat
    Menu_Header = colored('REMOTE EXPLOITATION', 'cyan', attrs=['bold'])
    print Menu_Header

    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. PAYLOAD GENERATORS & LISTENERS, Metasploit Msfvenom, and open source alternatives RATs like Pupy and Stitch',
        '#2. TOOLKITS, Social Engineers Toolkit',
        '#3. OTHER, Does not fit in any other category, USB Rubber Ducky Encoders, stuff like Virus-Total Safe-Checker',
        '#4. ***NEW***: FOREPLAY PROJECT, Easy-Mode Hacker Collaboration, gang up on single targets, easily generate Armitage Teamservers!'
    ]

    print ("\n\t".join(opt_List))

    print toolkits.green('\t' + opt_List[4])
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        payload_generators_listeners()
        three_remote_exploits_redesigned()
    elif opt_Choice == "2":
        os.system('clear')
        remote_exploit_toolkits()
        three_remote_exploits_redesigned()
    elif opt_Choice == "3":
        os.system('clear')
        remote_exploits_other()
        three_remote_exploits_redesigned()
    elif opt_Choice == "4":
        os.system('clear')
        foreplay()
        three_remote_exploits_redesigned()
    else:
        print colored('You have entered a invalid option','red')
        three_remote_exploits_redesigned()
    return


def APK_Malware_Injection():
    os.system('python /root/ArmsCommander/mobiledevices/APKmalwareInjector.py')
    main()
    return

def DIAMONDSHARK():
    os.system('python /root/ArmsCommander/mobiledevices/DIAMOND_SHARK/DS_Menu.py')
    main()
    return

def four_mobile_dev_hacking():
    Menu_Header = colored('MOBILE DEVICE HACKING', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0 Return to Main Menu',
        '#1. Android APK file Malware Injection',
        '#2. DIAMONDSHARK, Easy-to-use readaption of the Stagefright Exploit (mp4 file, shellcode injection)'
     ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        APK_Malware_Injection()
    elif opt_Choice == "2":
        DIAMONDSHARK()
        # MT_host_recon()
    else:
        print colored('You have entered a invalid option','red')
        four_mobile_dev_hacking()
    return

def cylon_raider():
    os.system('python /root/Cylon-Raider-Lite/Cylon_Raider_Main.py')
    main()
    return

def heavy_raider():
    os.system('python /root/ArmsCommander/wirelessattacks/Heavy-Raider/HeavyRaider.py')
    main()
    return

def router_sploit():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        'INSTALL. Install the RouterSploit Framework',
        '#1. Run the RouterSploit Framework'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION, or type INSTALL in all caps to install RouterSploit: "))

    if opt_Choice == "1":
        os.system('clear')
        os.system("gnome-terminal -e 'bash -c \"python /root/routersploit/rsf.py; exec bash\"'")
        main()
    elif opt_Choice == "INSTALL":
        os.system('clear')
        print 'Git Cloning RouterSploit into your Cylon-Raider Installation'
        os.system('cd /root')
        os.system('git clone https://github.com/reverse-shell/routersploit.git')
        print 'Routersploit install complete'
        main()
    return

def ARP_injection_test():
    os.system('airmon-ng start wlan1')
    cmd_String = "aireplay-ng -9 wlan1mon --ignore-negative-one"
    print cmd_String
    os.system(cmd_String)
    main()

    return

def hidden_network_decloaker():
    os.system('python /root/Cylon-Raider-Lite/sniffHidden.py')
    return

def mgt_ent_attacker():
    os.system('python /root/ArmsCommander/wirelessattacks/mgt_enterprise_cracker.py')
    return

def five_wireless_attacks(): # In the age of Cyberterrorism. Only the most cunning will survive.
    Menu_Header = colored('WIRELESS ATTACKS', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Cylon-Raider, automate wireless "Replay-Attacks" from the Aircrack-ng Suite',
        '#2. Cylon Heavy-Raider, automate the WPS PIN brute-forcing vulnerability with Reaver',
        '#3. Router-Sploit, Post-Exploitation hacking of APs that you cracked the passwords of',
        '#4. ARP Injection Test, seeing if your external wireless card is working properly',
        '#5. Hidden Network Decloaker, uncover hidden wireless APs',
        '#6. ***NEW*** DRADIUS WPA2-MGT/ENT (name tentative to change), impersonate Enterprise/Management/PEAP encrypted WPA2 Access Points, steal credentials!'
    ]
    print ("\n\t".join(opt_List))

    print toolkits.green('\t' + opt_List[6])

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('clear')
        cylon_raider()
        # MT_host_recon()
    elif opt_Choice == "2":
        os.system('clear')
        heavy_raider()
        # CornHarvester()
    elif opt_Choice == "3":
        os.system('clear')
        router_sploit()
        # NMap_Auto()
    elif opt_Choice == "4":
        os.system('clear')
        ARP_injection_test()
        # NMap_Custom()
    elif opt_Choice == "5":
        os.system('clear')
        hidden_network_decloaker()
        # SQLMap()
    elif opt_Choice == "6":
        os.system('clear')
        mgt_ent_attacker()
        five_wireless_attacks()
    else:
        print colored('You have entered a invalid option','red')
        five_wireless_attacks()

def aircrack():
    os.system('python /root/Cylon-Raider-Lite/CrackHead_Aircrack.py')
    main()
    return

def six_password_attacks():
    os.system('python /root/ArmsCommander/passwordattacks.py')
    main()
    return

def Violent_Python_Menu():
    os.system('python /root/ArmsCommander/booklearning/Violent-Python-POCs/Violent_Python_Menu.py')
    main()
    return

def Black_Hat_Python_Menu():
    print 'In Construction, Check back soon!'
    main()
    return

def seven_book_learning():
    Menu_Header = colored('BOOK LEARNING MENU', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Violent Python POCs',
        '#2. Black Hat Python POCs'
    ]
    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        main()
    elif opt_Choice == "1":
        os.system('clear')
        Violent_Python_Menu()
    elif opt_Choice == "2":
        os.system('clear')
        Black_Hat_Python_Menu()
        # MT_host_recon()

    else:
        print colored('You have entered a invalid option','red')
        seven_book_learning()
    return

# Rise, black amps tear the sky
# Feedback will free your mind and set you free
# Rise, black amps tear the sky
# Riff hewn altar wreathed in smoke and weed
#


def main():
    # os.system('cat /root/ArmsCommander/banners/banner_mainmenu.txt\n\n')
    Menu_Header = colored('MAIN MENU', 'cyan', attrs=['bold'])
    print Menu_Header
    opt_List = [
        '\n\t#0 Exit Program',
        '#1. Reconnaissance Tools & Vulnerability Scanners',
        '#2. Network Defenses & Traffic Monitoring',
        '#3. Remote Exploitation/Hacking',
        '#4. Mobile Device Hacking',
        '#5. Wireless Attacks',
        '#6. Password Attacks',
        '#7. Book Learning'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "1":
        os.system('clear')
        one_recon_and_vuln_scan()
    # elif opt_Choice == "0" or "EXIT" or "exit":
    #     print 'Exiting Program'
    #     exit(0)
    elif opt_Choice == "2":
        os.system('clear')
        two_net_defense_traffic_monitor()
    elif opt_Choice == "3":
        os.system('clear')
        three_remote_exploits_redesigned()
    elif opt_Choice == "4":
        os.system('clear')
        four_mobile_dev_hacking()
    elif opt_Choice == "5":
        os.system('clear')
        five_wireless_attacks()
    elif opt_Choice == "6":
        os.system('clear')
        six_password_attacks()
    elif opt_Choice == "7":
        os.system('clear')
        seven_book_learning()
    else:
        print colored('You have entered a invalid option','red')
        error_handling()
        main()
    return
main()

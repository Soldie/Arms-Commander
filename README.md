# Arms-Commander-Stable
Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6, originally intended to only perform the Reconnaissance and Enumeration Stages (it's role is dramatically expanded now). Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects. 

# Installation, Type the Following Commands to Easily Install in a Linux Box
We now have a official How-To-Install Video for Kali Linux, for those with ZERO familiarity with Linux/Debian/Ubuntu in general, check it out: https://raw.githubusercontent.com/tanc7/Arms-Commander/master/How-To-Videos/How-To-Install-Arms-Commander.webm, no audio
1. cd /tmp/
2. git clone https://github.com/tanc7/Arms-Commander
3. cd Arms-Commander/
4. chmod 777 autoInstallLinux.sh dependencyInstall.sh
5. ./dependencyInstall.sh # Required for installation of Python 2.7, and specifically Termcolor Python Module
6. ./autoInstallLinux.sh

ArmsCommander is now able to run from the Terminal or from the Desktop Launcher

# Running Arms Commander for the first time, open a terminal and type
ArmsCommander.py

# Uninstallation Instructions (Removes Desktop Launcher, the Terminal command, and /root/ArmsCommander directory, including log files)
1. cd /root/ArmsCommander
2. chmod 777 uninstall.sh
3. ./uninstall.sh

# Current Capabilities (From the Main Menu)
	#1. Battery One: URL RECON, Recon a webpage, Dig + Nslookup + Fierce DNS + Whois Lookup
	#2. Battery Two: LOCATE WEBAPP WEAKNESSES, Pop a smoke screen by flooding their Intrusion Detection System while simultaneously running a SQLMap and OWASP scanner attack
	#3. Battery Three: IP RECON via Port Scan using NMap and other tools
	#4. Battery Four: STANDARD DEFENSIVE MEASURES, activate Tor and Proxychains, all required monitoring tools
	#5. Battery Five: ANDROID APK MALWARE INJECTION, Inject a Metasploit Meterpreter Payload into a Android APK Installer File.
	#6. Battery Six: ACTVE NETWORK DEFENSES, terminate connections with NGrep and TCPKill, change your MAC address
	#7. Battery Seven: BOOTERS
	#8. Battery Eight: REMOTE EXPLOITATION, Metasploit, MSFVenom, Armitage, Veil-Evasion, Social Engineer Tookit
	#9. Battery Nine: BAD USB ATTACKS, Use the BadUSB Vulnerability to deliver undetectable attacks by thumbdrive
	#10. Battery Ten: Violent Python (From the Book) Working Proof of Concepts (POCs)

# Current Capabilities (Violent Python Menu)
	#1. SSH Server/Client Brute Forcer
	#2. Zip File Password Cracker (Better, Kali APT-Repo Alternative)
	#3. Wireless Network Credit Card Info Sniffer
	#4. Local FTP-Server Credential Sniffer
	#5. Exif Data Fetcher
	#6. Mitnick Attack Reenactment 

# Update History

# Alpha Version 0.0.5

1. Added a portion of still-working exploits as described by the author of Violent Python T.J. O'Connor, including but not limited to, a SSH Bruteforcer and a Credit Card Information Sniffer
2. Added /logs/ folder to save captured credentials

# Alpha Version 0.0.4

1. Added Keystroke Injection/BadUSB Attack Interface
2. Easy inject.bin generator for USB Rubber Duckies from Hak5 Shops
3. Forked in copies of ducky-flasher

# Alpha Version 0.0.3
1. Added the Ruby-based Android APK Malware Injection Module
2. Also forked over the required Java Signing Apps and required keys and certificates

# Why Isn't There a Windows Version?
So normally, as AC is a python script/program, then in theory it should work on Windows right? Well, no. And I can explain.

AC is a simple menu that automates several popular tools in Kali Linux. And it only works with Kali Linux tools, and requires it's specifications, like System-Level Root and it's unique upstream kernel. You most certainly can get it working on Ubuntu, but that requires a lot of customization and a lot of Linux-breaking commands. I'd say, you are much better off just installing a VM image of Kali Linux in accordance to their guidelines: https://www.kali.org/downloads/ and here: http://docs.kali.org/category/installation

# Do I need a official hard disk installation of Kali Linux?
For most users, never. The question is, do you want to end up breaking your HDD install of Kali Linux and being forced to reinstall everything and possibly lose your work? Does the benefits outweigh the costs? 

I have two installs of Kali. One is my HDD install on my laptop. And another is a VM image running on Hyper-V Server, with a Windows Server 2016 install acting as "Host".

If you have the following issues, then maybe you do require a HDD install of Kali Linux:
1. Password crackers like Aircrack-ng, JohnTheRipper, RainbowCrack running way too slowly, because it's a Virtual Machine image that cannot take advantage of the actual hardware. You might need a actual hard-disk install of Kali Linux.
2. Any external Wi-Fi card compatibility issues with VirtualBox + Kali VM Images. If you have trouble getting your external network card running and being detected normally, you MIGHT need to install a HDD copy. BUT, you should first consider just making a persistent USB installation. Now I know the official guide is a bit hard: http://docs.kali.org/downloading/kali-linux-live-usb-persistence but I personally felt that this older version of the guide: http://docs.kali.org/kali-dojo/03-kali-linux-usb-persistence-encryption, using fdisk and crypt was much better written.

*Note, I just noticed I am having a bit of difficulty finding the exact copy of the guide for easier creation of the USB Persistent Encrypted Partition. They all say the same thing, but I distinctly remember a blog-like guide with a little blue troll-looking creature as a logo. I can't find that link anymore. Meanwhile the original guides on the Kali Documentation seems like they have been updated. 

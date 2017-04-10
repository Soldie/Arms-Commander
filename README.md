# Arms-Commander-Stable
Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6, originally intended to only perform the Reconnaissance and Enumeration Stages (it's role is dramatically expanded now). Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects. 

# Installation, Type the Following Commands to Easily Install in a Linux Box
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

# Update History

# Alpha Version 0.0.6

The installation steps are still the same. Gitclone this repo's URL into a directory, run the dependency installer and autoinstaller scripts.

1. Added CornHarvester, the upgraded version of TheHarvester, allowing you to repeatedly harvest emails from a wordlist containing domain.com on each line so you can target them in a spearphishing attack
2. Added DIAMONDSHARK, a easy to use adaption of JDuck's StageFright Exploit targeting Android Devices using MMS. Generates a mp4 file containing nothing, uses a ARM Linux Command Shell that connects back to you. It also generates a handler.rc resource file for you to quickly set up your listener in Metasploit
3. In previous versions, added EasyPeasey, named after Mr. Leslie Chow from The Hangover series, allows you to quickly generate msfvenom payloads to your liking
4. Greatly improved speediness and usability by having a few of the default tools automatically generate a logfile in your /root/ArmsCommander/logs folder

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

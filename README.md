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

# Optional, Pupy Installation
https://github.com/n1nj4sec/pupy/wiki/Installation
Pupy is a alternative RAT based on Python that may increase your odds of successfully evading antivirus. 
Installation is not required, however, You will lose out on it's features

After several tests with the install, I have came to the conclusion that Pupy is best handled by installing it standalone because it generates very sensitive data including SSL keys made for it's payloads.

However, ArmsCommander is designed to interface with Pupy via a /root/ directory installation. So in other words... (to isntall Pupy),

1. cd /root/
2. git clone https://github.com/n1nj4sec/pupy.git pupy
3. cd pupy
4. git submodule init
5. git submodule update
6. pip install -r requirements.txt

At this point you are done. 

Arms Commander will naturally run Pupy from it's Menu assuming that:
1. Pupy Server is at /root/pupy/pupy/pupysh.py
2. Pupy Payload Generator is at /root/pupy/pupy/pupygen.py

Please double check. That the above instructions are followed perfectly. This is critical because Pupy relies on other packages, such as Empire for Powershell based payloads.

# Uninstallation Instructions (Removes Desktop Launcher, the Terminal command, and /root/ArmsCommander directory, including log files)
1. cd /root/ArmsCommander
2. chmod 777 uninstall.sh
3. ./uninstall.sh

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

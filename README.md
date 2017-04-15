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

# How to Install and Use Pupy, the alternative Python-based RAT (Remote Access Trojan)

# Benefits
1. Harder to detect, not as common as Metasploit’s Meterpreter
2. A lot of work has been put into this project by the repo’s developer Ninjasec
3. Carries many of the same evasion tools that Metasploit uses, including staged encryption
4. Similar command and control scheme
5. For those with a minimal amount of Python knowledge, very easy to debug issues

# Installation (Pupy)
It is best to install Pupy as a standalone install, I tried to automate it, and it caused more headaches than I can imagine

It’s just a few things on the terminal. Don’t worry, no keyboard breaking raage for you!

	git clone https://github.com/n1nj4sec/pupy.git pupy
	cd pupy
	git submodule init
	git submodule update
	pip install -r requirements.txt 

# Post install modifications
Currently there are two bugs
1. The Linux binary templates are missing, I can’t fix that (but Python payloads work out of the box  against Linux boxes). And #1 isn’t even necessary to hack into Linux boxes, I will show you either in a different video or this one.
2. There is a file-path error that I can show you how to fix right now. If you don’t fix it, it will spit out File Not Found Errors when you attempt to generate payloads. https://github.com/tanc7/Arms-Commander/blob/master/README.md

Basically, for #2, we are going to give it a more “complete” file path. Since it can’t see the “credentials.py” file right out of the box. Just one line to modify code on. 

I am going to use Atom for this, but you can use anything you like or use control find or something

There is a error in the payload generator file on line #114

Change 
		
		creds_src=open("crypto/credentials.py","r").read()

into 
		
		creds_src=open("/root/pupy/pupy/crypto/credentials.py","r").read()

# Uninstallation Instructions (Removes Desktop Launcher, the Terminal command, and /root/ArmsCommander directory, including log files)
1. cd /root/ArmsCommander
2. chmod 777 uninstall.sh
3. ./uninstall.sh

# Update History

# Alpha Version 0.0.7

1. First step in integration with alternative RAT, Pupy.

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

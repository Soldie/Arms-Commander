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
How to install Pupy: https://github.com/tanc7/Arms-Commander/raw/master/How-To-Videos/How-To-Install-Pupy.webm
It is best to install Pupy as a standalone install, I tried to automate it, and it caused more headaches than I can imagine

It’s just a few things on the terminal. Don’t worry, no keyboard breaking raage for you!

	cd /root
	git clone https://github.com/n1nj4sec/pupy.git pupy
	cd pupy
	git submodule init
	git submodule update
	pip install -r requirements.txt

How To Interact with Pupy Shell: https://github.com/tanc7/Arms-Commander/raw/master/How-To-Videos/How-To-Interact-With-Pupy-Server-Shell.webm
# Post install modifications
Currently there are two bugs
1. The Linux binary templates are missing, I can’t fix that (but Python payloads work out of the box  against Linux boxes). And #1 isn’t even necessary to hack into Linux boxes, I will show you either in a different video or this one.
2. There is a file-path error that I can show you how to fix right now. If you don’t fix it, it will spit out File Not Found Errors when you attempt to generate payloads. https://github.com/tanc7/Arms-Commander/blob/master/README.md

Basically, for #2, we are going to give it a more “complete” file path. Since it can’t see the “credentials.py” file right out of the box. Just one line to modify code on.

I am going to use Atom for this, but you can use anything you like or use control find or something

There is a error in the payload generator file on line #114

		/root/pupy/pupy/pupygen.py

Change

		creds_src=open("crypto/credentials.py","r").read()

into

		creds_src=open("/root/pupy/pupy/crypto/credentials.py","r").read()

# Uninstallation Instructions (Removes Desktop Launcher, the Terminal command, and /root/ArmsCommander directory, including log files)
1. cd /root/ArmsCommander
2. chmod 777 uninstall.sh
3. ./uninstall.sh

# Update History

# Alpha Version 0.0.8, "DLLA" or "Don't Look Like Ass Update" has been uploaded to GitHub

Overall it's not a update for the end-user (Unless you are writing in Python). It is something like, "LTS" Long-Term Support preparations to make debugging easier, and reconfiguring the menu much simpler.

In recent headlines, there were several major events that might cause me to take a further interest in "zero-day exploits", and I think all of us are double-timing to catch up with the new news updates.

In a short while, I will also update the README and How-To-Videos, but none of the original tools in the videos have been altered. Its that their location has been changed in the menu to make room. 

Major changes

1. Pruning of the entire menu tree
2. There are now seven categories to choose from rather than 11. Two of the seven are all new tools that were part of my other projects (Wireless Attacks being one of them)
3. Reorganized directory structure
4. Automatic logging now enabled for a majority of the recon packages
5. Several bugs fixed
6. Dramatic shortening of source code and commented out code
7. Several changes, including... Automatic Starting of Tor when you run SQLMap. Furthermore all NMap commands are now proxychained by default. 

From now on, the Menus will be rebuilt back from the ground up to avoid clutter and will be strictly organized into the following subtypes

# 1. Reconnaissance Tools & Vulnerability Scanners
	#1. Multi-Tool Single Host Recon, use Dig, NSLookup, fierce, and theharvester against a single target
	#2. CornHarvester, mass-harvest emails for phishing/Spear-Phishing
	#3. NMap Scans (preset for maximum information discovery), starts with FIN scan, then XMAS scan, and finally a comprehensive scan
	#4. Run SQLMap (Automatically set to route traffic through Tor)
	#5. OWASP Zaproxy (Alternative vulnerability scanner, much faster than SQLMap)
	#6. BurpSuite

# 2. Network Defenses & Monitoring
	#0 Return to Main Menu
	#1. Tor + Proxychains, conceal your outbound traffic
	#2. Network Monitoring Tools, p0f, Snort, and view active network connections
	#3. Cover your tracks, clear your bash history and wipe your thumbnails cache
	#4. TCP Kill a connection by host, IP, or port
	#5. NGrep or "Network Grep", investigate a suspicious connection
	#6. MacChanger, change your network card MAC address temporarily
	#7. Fuser, identify and kill processes within a port range
	#8. IDS Flooder, overwhelm a Intrusion Detection System with false-flag DDoS attacks to draw attention away from your actual activity

# 3. Remote Exploitation/Hacking 
	#0. Return to Main Menu
	#1. Metasploit Framework, with a Manual-Start Script to overcome any database init issues
	#2. Armitage
	#3. Easy-Peasey, msfvenom payload generator
	#4. Veil-Evasion, changes signature of msfvenom type payloads
	#5. Social Engineers Toolkit (SET), a expansive toolkit by itself that covers spearphishing attacks to SMS spoofing to Arduino-attacks
	#6. Pupy, Cross-Platform, Pythonic version of a Remote Access Trojan (RAT) with abilities that are comparable/superior to Meterpreter shells, with added benefits of being rarer and therefore harder to detect, and supports powershell injection
	#7. Dont Patch Me Bro :(, the easy-mode inject.bin generator for Hak5 USB Rubber Duckies

(Spearphishing and payload generators for example) --- Considering including the BadUSB and Keystroke Injection Type Attacks into this, since it ultimately results in remote exploitation
# 4. Smartphone/Mobile Device Hacking
	#0 Return to Main Menu
	#1. Android APK file Malware Injection
	#2. DIAMONDSHARK, Easy-to-use readaption of the Stagefright Exploit (mp4 file, shellcode injection)

# 5. Wireless Attacks (Not even implemented, but it's basically a port of Cylon-Raider-Lite into AC: DLLA)
	#0. Return to Main Menu
	#1. Cylon-Raider, automate wireless "Replay-Attacks" from the Aircrack-ng Suite
	#2. Cylon Heavy-Raider, automate the WPS PIN brute-forcing vulnerability with Reaver
	#3. Router-Sploit, Post-Exploitation hacking of APs that you cracked the passwords of
	#4. ARP Injection Test, seeing if your external wireless card is working properly
	#5. Hidden Network Decloaker, uncover hidden wireless APs

# 6. Password Attacks
	#0 Return to Main Menu
	#1. Aircrack-ng, crack captured WPA handshakes
 
(for now, considering just leaving it at the Wireless attack category, there is no GPU support until I see a more enthusiatic community (the hashcat crowd doesn't seem to be "cool with Kali" rrecently and I am not here to break anyone's machine from a botched video driver install))
# 7. "Book Learning", 
	#0. Return to Main Menu
	#1. Violent Python POCs
	#2. Black Hat Python POCs

still-working and useful tools adapted from literature such as Violent Python and Black Hat Python

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

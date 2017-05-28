# Arms-Commander-Stable
Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6. Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects.

# Update: Counter-Forensics Suite, Top Metasploit Plugins, TSOCKS. and more!

		1. TSocks (Tor-Socks) now auto-installed as a alternative to using and configuring proxychains, simply preclude your command with "tsocks <cmd>" to automatically route your traffic through Tor, like 'tsocks nmap <target>'"
		2. Fail2Ban is recognized as a critical component for remote servers in the cloud, due to near-constant SSH brute-forcing attempts, and is now automatically installed and auto-configured
		3. A bug has been fixed where hashcat utilities failed to download and install. It is now automatically performed through the setup.py file, simply type "python setup.py"
		4. The Metasploit Plugins suite from DarkOperator on GitHub is now automatically installed and dropped into your metasploit installation, to use, type 'load pentest' in msfconsole and type 'help' to see a list of commands on the top.
		5. Mass-mailer attacks are recognized as a crucial method in getting reverse shells to open, this current AC installation includes a Python HTML mass-mailer


As usual, the dev for ArmsCommander rigorously tests his modules before ever releasing it. However, some bugs make it through and he will jump on it immediately if he sees one.



# Update: CSV Files Generation, introduction of Under-the-Hood Libraries and Python Modules

**Added additional parsing options for reconned hosts, and the toolkits under the /recon folder. It will automatically generate a CSV file** in your /logs directory for the following tools

		1. NMap --> CSV logfile
		2. CornHarvester --> Two CSV Files, (A) Email Addresses and (B) Hosts related to the domain

**The same goes for password attacks**

		1. Added additional options for Pyrit Analyze, it will now generate a csv logfile that contains...
			a. Handshakes captured
			b. BSSID, ESSID
			c. MAC addresses of connected clients
			d. Location of your capture file
		2. This allows users to quickly sort through heaps of useless *.cap files, or uninteresting capture files, and allows them to quickly start cracking the USEFUL Wi-Fi handshakes

The steps of using this option is as follows...

	1. Go capture the WPA2 handshake using Airodump and Aireplay (or use my Cylon-Raider Toolkit)
	2. Come back home, run all of the *.cap files through Pyrit Analyze
	3. Load the generated *.csv file in LibreOffice Calc, Google Sheets, or Microsoft Excel. Weed out the crappy capture files.
	4. Load the good capture file list into Hashcat (this comes preinstalled with a *.cap to *.hccapx converter). 
	5. Finally, run "Cocaine Factory", in this toolkit, which automatically loads the hashcat file into hashcat, and queues the remaining ones with a wordlist, so you can afk and keep cracking new hashes.

All of this can be accessed from:

Main Menu
--> #6. Password Attacks
----> #2. Hashcat Interactive Menu Suite

Menu Display:

	#0. Main Menu
	#1. **Mass-Convert WPA2-PSK handshakes into Hashcat Format HCCAPX**
	#2. **Mass-Autoload .hccapx format files into hashcat**
	#3. Video card tuner for NVIDIA CUDA core GPUs and GPU monitoring systems
	#4. Dump cracked hashes
	#5. Run, INTER-CAT, the interactive menu to simplify the usage of hashcat
	#6. **Pyrit-Analyze Capture Files**, check whether or not your capture files have valid EAPOL handshakes
	#CUDAINSTALL. Run the CUDA Setup Suite to install drivers and configure fresh NVIDIA GPU systems for password cracking
Enter a OPTION: 


**All five steps, involve using the edited wordlist, a option to edit the wordlist with leafpad will be listed in the menu options**

# COMMENCEMENT OF THE PYTHON-MIRAI PROJECT

After realizing that there is no Pythonic adaption of the open source Mirai Botnet source code, I have decided to begin a long-term reverse engineering project, to translate or convert all of the Mirai Botnet Source Code into Python.

This will take significantly longer than usual for me to stay updated on, readers may follow my notes here on what I found out about how Mirai works:
https://github.com/tanc7/Arms-Commander/blob/master/remoteexploits/Mirai_Python_Project/notes.md



# Installation
Instead of fiddling with uncertain terminal commands, for those new Linux users, you can now simply download ONE FILE and run that to automate the setup harmlessly.

> just run 'python setup.py' in /$PATH/Arms-Commander

		1. Download "setup.py" which is the Experimental Arms-Commander Python Installer.
		2. Run the script, type 'python setup.py'
		3. It will automate the Git Cloning process for you as well as the git submodule inits and updating and python module installations
		4. It will also warn you to back up the log files provided by previous installs of Arms-Commander. You will have to type "CONTINUE" in all caps and hit [Enter] to proceed with replacing the old AC with the new AC
		5. As soon as it is done installing the prerequisites, it will automatically start ArmsCommander's Console. At this point you can start AC with the terminal command 'ArmsCommander.py' or double click the launcher on your /root/Desktop directory.

# Important Disclaimer about CUDA Setup Utility

Because of the

1. proprietary factor of NVIDIA graphics drivers

2. The volatile environment of buggy updates between all Linux and derivatives

3. Various adaptions and buggy code in Arms-Commander that i am trying to fix as one person

4. And that no one's machine is exactly alike (different drivers working for different NVIDIA models, breaking others, maybe requiring alternative desktop environments like XFCE for certain installations)

Its safe to assume that this utility can regularly break your machine.

What it does do, is attempt to automate the basic meat and potatoes of the NVIDIA driver installation process for Linux.

Technical support is lacking and incomplete.

You are in very dark waters, be warned.

# (Manual) Installation, Type the Following Commands to Easily Install in a Linux Box
1. cd /tmp/
2. git clone https://github.com/tanc7/Arms-Commander
3. cd Arms-Commander/
4. chmod 777 autoInstallLinux.sh dependencyInstall.sh
5. ./dependencyInstall.sh # Required for installation of Python 2.7, and specifically Termcolor Python Module
6. ./autoInstallLinux.sh

# Uninstallation Instructions (Removes Desktop Launcher, the Terminal command, and /root/ArmsCommander directory, including log files)
1. cd /root/ArmsCommander
2. chmod 777 uninstall.sh
3. ./uninstall.sh

# 1. Reconnaissance Tools & Vulnerability Scanners
	#0. Return to Main Menu
	#1. Multi-Tool Single Host Recon, use Dig, NSLookup, fierce, and theharvester against a single target
	#2. CornHarvester, mass-harvest emails for phishing/Spear-Phishing
	#3. NMap Scans (preset for maximum information discovery), starts with FIN scan, then XMAS scan, and finally a comprehensive scan
	#4. Run SQLMap (Automatically set to route traffic through Tor)
	#5. OWASP Zaproxy (Alternative vulnerability scanner, much faster than SQLMap)
	#6. BurpSuite
	#7. OUTPUT/BACKUP ALL DATA collected from Multi-Tool, CornHarvester, and NMap

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
	#1. PAYLOAD GENERATORS & LISTENERS, Metasploit Msfvenom, and open source alternatives RATs like Pupy and Stitch
	#2. TOOLKITS, Social Engineers Toolkit, Metasploit, Easy-Peasey Payload Generator, etc.
	#3. OTHER, Does not fit in any other category, USB Rubber Ducky Encoders, stuff like Virus-Total Safe-Checker

# 4. Smartphone/Mobile Device Hacking
	#0 Return to Main Menu
	#1. Android APK file Malware Injection
	#2. DIAMONDSHARK, Easy-to-use readaption of the Stagefright Exploit (mp4 file, shellcode injection)

# 5. Wireless Attacks
	#0. Return to Main Menu
	#1. Cylon-Raider, automate wireless "Replay-Attacks" from the Aircrack-ng Suite
	#2. Cylon Heavy-Raider, automate the WPS PIN brute-forcing vulnerability with Reaver
	#3. Router-Sploit, Post-Exploitation hacking of APs that you cracked the passwords of
	#4. ARP Injection Test, seeing if your external wireless card is working properly
	#5. Hidden Network Decloaker, uncover hidden wireless APs


# 6. Password Attacks
	#0 Return to Main Menu
	#1. Run Cylon-Raider, Interactive Menu for Aircrack-ng Replay Attacks
	#2. Run the Hashcat Interactive Menu Suite, including the interactive CUDA GPU driver installers


# 7. "Book Learning",
	#0. Return to Main Menu
	#1. Violent Python POCs
	#2. Black Hat Python POCs


# How to Install and Use Pupy, the alternative Python-based RAT (Remote Access Trojan)
You can install Pupy with my automated installer. Either you can access it from the ArmsCommander Menu or... run the installer directly as so... in Terminal type:

> python /root/ArmsCommander/remoteexploits/Pupy_Menu.py

On the interactive menu type

> INSTALL

and hit [ENTER]

# Benefits
1. Harder to detect, not as common as Metasploit’s Meterpreter
2. A lot of work has been put into this project by the repo’s developer Ninjasec
3. Carries many of the same evasion tools that Metasploit uses, including staged encryption
4. Similar command and control scheme
5. For those with a minimal amount of Python knowledge, very easy to debug issues

# 6. Most importantly, You can combine Pupy and Metasploit Shells together as a "Insurance Policy", one will upload and/or execute the other, allowing you to resurrect dead Shells

From Pupy (bring back Meterpreter), after gaining SYSTEM privileges:

> run manage/upload <local dir file> <remote dir>

> run admin/interactive_shell

> C:\$PATH\> start <meterpreter.exe>

And vice versa, from a remaining Meterpreter shell.... after you getsystem:

> sessions -i <session>

> upload <local dir> <remote dir>

> execute <pupyshell.exe>

# Arms-Commander, now has a included Python Script that will automatically install Pupy, initialize/update submodules, and install the required Python modules for you.
		Run ArmsCommander in terminal 'ArmsCommander.py'
		Select #3 'Remote Exploitation'
		Select #6 'Pupy'
		Type 'INSTALL' and hit [Enter]
		Grab yourself some coffee, it's gonna take a while!

# Warning: On remote/cloud server usage for Pupy (& also Stitch's AES Encrypted payloads)

It became apparent from extensive testing, that if you are to use Amazon AWS to act as a remote proxy listener (or what the CIA calls "LPs" or "Listening Posts"...
The "manufacturing process of the payload" MUST be conducted on the LISTENER.
You cannot just, make a payload on your laptop, and expect your remote server to listen to the connection
This is due to the way that the SSL certs are negotiated. It is meant to conceal your backdoor traffic and avoid alerting the IT dept.
However, that also means the SSL certs are UNIQUE to your machine. Hence, no one else, not even a alternative device could "hijack" the session.

# Arms-Commander-Stable
Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6, originally intended to only perform the Reconnaissance and Enumeration Stages (it's role is dramatically expanded now). Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects.

# Coming Soon: Integration with Stitch
Once I figure out these damned installation errors, Error Code 1 in Pip?!? I believe it's permissions based but... i already Chmodded everything with 777?!?

# (NEW) Completely automated installer written in Python

Instead of fiddling with uncertain terminal commands, for those new Linux users, you can now simply download ONE FILE and run that to automate the setup harmlessly.

		1. Download "Xperi_Setup.py" which is the Experimental Arms-Commander Python Installer.
		2. Run the script, type 'python XPeri_Setup.py'
		3. It will automate the Git Cloning process for you as well as the git submodule inits and updating and python module installations
		4. It will also warn you to back up the log files provided by previous installs of Arms-Commander. You will have to type "CONTINUE" in all caps and hit [Enter] to proceed with replacing the old AC with the new AC
		5. As soon as it is done installing the prerequisites, it will automatically start ArmsCommander's Console. At this point you can start AC with the terminal command 'ArmsCommander.py' or double click the launcher on your /root/Desktop directory.

		NOTE: I also included a easy-installer for Pupy as well, the alternative Python-based RAT provided by NinjaSec. I spent all day adapting to the new syntax and learning a few tricks on getting terminal commands (particularly chdir) to work right. Follow the on screen instructions to learn how, it's just another single command!

That is the best that I can do for Pupy easy-install. Because Pupy generates unique SSL keys that are special just to your personal machines. Failing to authenticate means that none of the features will work. Pupy must be installed by the end-user by themselves. Plus you definitely don't want to lose those credentials!

# (Manual) Installation, Type the Following Commands to Easily Install in a Linux Box
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

# Warning: On remote/cloud server usage for Pupy

It became apparent from extensive testing, that if you are to use Amazon AWS to act as a remote proxy listener (or what the CIA calls "LPs" or "Listening Posts"...
The "manufacturing process of the payload" MUST be conducted on the LISTENER.
You cannot just, make a payload on your laptop, and expect your remote server to listen to the connection
This is due to the way that the SSL certs are negotiated. It is meant to conceal your backdoor traffic and avoid alerting the IT dept.
However, that also means the SSL certs are UNIQUE to your machine. Hence, no one else, not even a alternative device could "hijack" the session.

It makes configuring my remote listener a pain. Because I have to use ArmsCommander to make the file on the remote server, then go back and download it back into my machine, embed a payload, start up listener, test it, etc.

The credentials are automatically stored in your GNOME keyring, but I have failed to proper copy the creds over into my AWS instance for some reason.


# Uninstallation Instructions (Removes Desktop Launcher, the Terminal command, and /root/ArmsCommander directory, including log files)
1. cd /root/ArmsCommander
2. chmod 777 uninstall.sh
3. ./uninstall.sh




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

# Arms-Commander-Stable

Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6. Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects.

# Dorah the Explorah Update.

# Imma explorah your booty!**

Thanks to the positive reception from the Las Vegas Python coding Meetup, I have released the official version of the nmap scriptor, as Dorah the Explorah for Arms Commander.

You can find it under the recon menu.

![](http://vignette3.wikia.nocookie.net/doratheexplorer/images/2/2f/Dora-the-explorer.png/revision/latest?cb=20130917150432)

**Features**
1. All 568 nmap scripts are available as both selectable scripts and help menus with only three button presses.

2. Category scanning is available, like all vulnerability scanning, Or try all exploits

3. Simple automatic integration with Metasploit Framework's db_nmap via resource scripts, either option will save your scans. Either in the HOSTS database or as three different file formats in your log directory.

4. Automatic anonymization via tor and tsocks

# New Development: The Automatic NMap Scriptor
https://github.com/tanc7/Arms-Commander/blob/master/recon/TEST_db_nmap_with_scripts.py

Name tentative to change. Because it really sounds stupid as it is. **However, I managed to incorporate all 568 Unique NMap scripts into a easy-to-use and selectable, point-n-shoot, NMap scanner.** Do not worry, I didn't really type all that 1,800+ lines of code. I wrote another lame program, called list_writer.py that automatically generates the if,elif,else statements, and the user UI menu for me in separate text files.

To use this (since as of right now, it is still not ready for release, and therefore not added to the actual ArmsCommander Menu), type the following commands:

	"cd /root/ArmsCommander/recon/"
	"python TEST_db_nmap_with_scripts.py"

A second console window will pop up, connecting you to the Tor network. Go ahead and minimize that.

	1. Now Select "3. run a NMap script INDIVIDUALLY"

	2. Go through the massive options, all 568 types of NMap scans spanning across several categories. Type the number to continue

	3. Select either/or:
	    #1. Metasploit + Tor Socks proxy
	    #2. Regular NMap + Tor Socks proxy

	4. Enter a IP address, IP range, hostname, website URL and press [Enter]

Now go make a sandwich, it's gonna take a while (hours). Certain NMap scripts will take longer than others.

# Update: Counter-Forensics Suite, Top Metasploit Plugins, TSOCKS. and more!

For the most part this update is another back-end upgrade. However, visually for the user they may notice a few key differences

	1. TSocks (Tor-Socks) now auto-installed as a alternative to using and configuring proxychains, simply preclude your command with "tsocks <cmd>" to automatically route your traffic through Tor, like 'tsocks nmap <target>'"
	2. Fail2Ban is recognized as a critical component for remote servers in the cloud, due to near-constant SSH brute-forcing attempts, and is now automatically installed and auto-configured
	3. A bug has been fixed where hashcat utilities failed to download and install. It is now automatically performed through the setup.py file, simply type "python setup.py"
	4. The Metasploit Plugins suite from DarkOperator on GitHub is now automatically installed and dropped into your metasploit installation, to use, type 'load pentest' in msfconsole and type 'help' to see a list of commands on the top.
	5. Mass-mailer attacks are recognized as a crucial method in getting reverse shells to open, this current AC installation includes a Python HTML mass-mailer installation (go to the menu and type INSTALL)
	6. There are multiple un-implemented modules to Cylon-Raider & Raider-Lite, as a result of the failed Missile-Lock Project. You can fiddle with them as you wish.


As usual, the dev for ArmsCommander rigorously tests his modules before ever releasing it. However, some bugs make it through and he will jump on it immediately if he sees one.

# COMMENCEMENT OF THE PYTHON-MIRAI PROJECT

After realizing that there is no Pythonic adaption of the open source Mirai Botnet source code, I have decided to begin a long-term reverse engineering project, to translate or convert all of the Mirai Botnet Source Code into Python.

This will take significantly longer than usual for me to stay updated on, readers may follow my notes here on what I found out about how Mirai works: https://github.com/tanc7/Arms-Commander/blob/master/remoteexploits/Mirai_Python_Project/notes.md

# Installation

Instead of fiddling with uncertain terminal commands, for those new Linux users, you can now simply download ONE FILE and run that to automate the setup harmlessly.

    just run 'python setup.py' in /$PATH/Arms-Commander

	1. Download "setup.py" which is the Experimental Arms-Commander Python Installer.
	2. Run the script, type 'python setup.py'
	3. It will automate the Git Cloning process for you as well as the git submodule inits and updating and python module installations
	4. It will also warn you to back up the log files provided by previous installs of Arms-Commander. You will have to type "CONTINUE" in all caps and hit [Enter] to proceed with replacing the old AC with the new AC
	5. As soon as it is done installing the prerequisites, it will automatically start ArmsCommander's Console. At this point you can start AC with the terminal command 'ArmsCommander.py' or double click the launcher on your /root/Desktop directory.

# Important Disclaimer about CUDA Setup Utility

Because of the

    proprietary factor of NVIDIA graphics drivers

    The volatile environment of buggy updates between all Linux and derivatives

    Various adaptions and buggy code in Arms-Commander that i am trying to fix as one person

    And that no one's machine is exactly alike (different drivers working for different NVIDIA models, breaking others, maybe requiring alternative desktop environments like XFCE for certain installations)

Its safe to assume that this utility can regularly break your machine.

What it does do, is attempt to automate the basic meat and potatoes of the NVIDIA driver installation process for Linux.

Technical support is lacking and incomplete.

You are in very dark waters, be warned.
# (Manual) Installation, Type the Following Commands to Easily Install in a Linux Box

    cd /tmp/
    git clone https://github.com/tanc7/Arms-Commander
    cd Arms-Commander/
    chmod 777 autoInstallLinux.sh dependencyInstall.sh
    ./dependencyInstall.sh # Required for installation of Python 2.7, and specifically Termcolor Python Module
    ./autoInstallLinux.sh

# Uninstallation Instructions (Removes Desktop Launcher, the Terminal command, and /root/ArmsCommander directory, including log files)

    cd /root/ArmsCommander
    chmod 777 uninstall.sh
    ./uninstall.sh

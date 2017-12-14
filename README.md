# Arms-Commander-Stable

Malware Suite/Menu designed for "Speedy and No-Mistakes Penetration Testing", written in Python 2.7.13 and tested on Kali Linux 4.6. Requires Python 2.7 + Pip + Termcolor Module. All code is entirely free to be used in your own projects.

# December 13th, Upcoming Update After Some Additional Coding and Testing.
# Improving and Honing your Hacking Abilities by Modifying the Routersploit Shell

After action report, Wednesday, December 13th, 2017.

I have successfully managed to take control of the RouterSploit Shell By passing commands through the their Shell API using the standard Python 2.7 console.

What this means, is that**I can createa a FULLY AUTONOMOUS Raspberry Pi that is designed to attack wireless networks with cracked passwords using the scanners/autopwn module.** The Pi will be the one "typing the commands" into RouterSploit using carefully timed Python scripts, cronjobs, and bash shell commands.

How the RouterSploit Shell works is that it has several sub-components that make up the terminal:

1. A **primary, Routersploit Interpreter Shell** that makes up several python scripts
2. A secondary, **lower-in-privilege Interpreter Shell known as "BaseInterpreter"** that does most of the contract between the user and the toolkit. It is represented as a class-object in the file Interpreter.py and shell.py
3. Finally a **SSH-Interactive Shell that works behind the scenes.** The purposes of this is unknown but I noticed it performs a lot of HTTP lifting as some sort of offensive back-end. This one may be the one with the directory traversal tactics and HTTP brute-forcing modules for Routersploit.


**['LockedIterator', '__builtins__', '__doc__', '__name__', '__package__', 'boolify', 'command', 'exceptions', 'exploits', 'http_request', 'index_modules', 'Interpreter', 'modules', 'multi', 'mute', 'payloads', 'print_error', 'print_info', 'print_status', 'print_success', 'print_table', 'printer', 'random_text', 'routersploit', 'sanitize_url', 'shell', 'ssh_interactive', 'test', 'tokenize', 'utils', 'validators', 'var', 'wordlists']**

Note: The BaseInterpreter appears to be part of some naming convention for their framework. For example, there are BaseExploits and BaseScanners, the latter of which is the backbone of the scanners/autopwn module.

As a user, you can actually interact with ALL THREE SHELLS at the same time right now to give it customized commands and background jobs, by downloading the official Routersploit Repo: 

and then  navigate to the module tree directory (for me it's in /root/Documents)
**
		**cd /root/Documents**

And activate python and immediately import the modules
**	


	1.>>>python
	
	2.>>>import routersploit
	
	3.>>>from routersploit import *
	
	4.>>>import __future__
	
	5.>>>import __builtin__
	
	6.>>>from __builtin__ import *
	
	7.>>>import routersploit.modules.utils
	
	8.>>>from __future__ import absolute_import
	
	9.>>>Interpreter.BaseInterpreter()
	
	10.>>>[<routersploit.Interpreter.BaseInterpreter object at 0x7fb92ac76510>]
	
	11.>>>Interpreter.BaseInterpreter(__init__)
	
If you are lost, don't forget you use your help(OBJECT) and dir(OBJECT) commands.

Also the memory address on the second to last line is a indication that the command worked and is running. You can alt-tab out and check your Routersploit.log to confirm that it is running.

But what I found was this one command, which after a bit of tinkering, was fully enabled to allow me to integrate my scripts and software with theirs and allow me to push commands to Routersploit to give it a job to do.

**Interpreter.RoutersploitInterpreter().commands()**

This is the most basic of the RSF Shell commands, all it does is query the shell to tell us all of the available commands. And the unordered array was the output. 

**['back', 'check', 'exec', 'exit', 'exploit', 'help', 'run', 'search', 'set', 'setg', 'show', 'unsetg', 'use']***


All of this was discovered by typing commands into the Python shell. That means it should be as easy as importing the Routersploit modules into your own Python programs.

The syntax for this, and other subsequent important commands comes in this format...

**Interpreter.RoutersploitInterpreter().action('CMD', args, xargs)**

Everything that was on the top of that Python list, can be executed through this Interpreter, as long as you IMPORT the right modules! As it turns out, there was a lapse in organization for the RSF development, and I spent about two yhours looking for the other modules to import to give the shell full functionality. But it seems current progress points is that they are trying hard to merge two different designs for their back-end together. 

Here is a sample of some syntax.


starts up the Interpreter, basically the shell started.

****Interpreter.RoutersploitInterpreter().start()***

This is actually the auto-tab-completion module for RouterSploit.

***BaseInterpreter.available_modules_completion('payloads')***

This is the equivalent of typing "Show Targets" in Metasploit.

***Interpreter.utils.module_required._show_devices('devices')***

This is what happens when you type "show scanners" in the RSF shell. The opt-parsing code immediately sends it to it's own submodule/process. 

***Interpreter.utils.module_required.__show_modules('scanners')***

When you type "use scanners/autopwn" in Routersploit

***Interpreter.BaseInterpreter().command_use('scanners/autopwn')***

This is how you can dump the Routersploit logs. Note the lower-case PRINT command on the left.

***print Interpreter.RoutersploitInterpreter(BaseInterpreter).history_file***

Even if you didn't know the module's programming syntax, you can still directly-inject commands into the parse_line(cmd) module. This was the earliest moment I could find a reliable injection point for commands.

***Interpreter.BaseInterpreter().parse_line("show payload)***


The next step up is calling the command_handler() to have it review the parsed user input. If you fail to inject a command into the parse_line function, a less reliable but decent second try is injecting the command into the get_command_handler() function.

***Interpreter.BaseInterpreter(get_command_handler('show'))***

# The auto exploiting Rpi...

Any assailant will not look suspicious at all as long as the Pi is powered on  and the attacker or "pentester" should just be walking around staying within wireless range. Now that I have found a breakthrough to createa a fully-automated initial exploitating Pi I think it's your turn to find a useful for this too ;).

To create a auto-exploiting Raspberry Pi, one would simply (after much testing and confirmation!!!)....

	Interpreter.BaseInterpreter.command_use('scanners/autopwn')
	Interpreter.RoutersploitInterpreter().commands('set TARGET 192.168.1.1')
	Interpreter.RoutersploitInterpreter().commands('set PORT 80')
	Interpreter.RoutersploitInterpreter().run('scanners/autopwn')***
	

It's much like handling a "pentest drop-box". But this time, the Pi is completely automated and ordered to exploit and post-exploit it's targeted victims

**Furthermore I have completed approximately 90% of the rest of the work that is meant to be added to the Pi or to compliment the gear of "wireless pentesters". For example...**

1.**A fully autonomous password-cracking rig**that is automated by cronjobs, Python scripts, and shell scripts. It handles the process of converting captured WPA handshakes into a hashcat compatible format, and will automataically queue and begin brute-forcing (dictionary attack style) as soon as it reboots. It applies a improved version of my hashcat add-ons that I put into Arms-Commander.

2. A **completely automatic, cracked-password sorting and credential installation service**. What I mean is, at a push of a button, it will parse the default HashCat potfile at /root/.hashcat/hashcat.potfile (for Kali Linux installations) to get rid of duplicate entries and false-positives.

And then "installs" the credentials onto your nearest mobile device by copying and appending the login information to your /etc/wpa_supplicant/wpa_supplicant.conf

As soon as you approach the area of your target that you are returning to, your network-manager should have already connected you to the target, ready for exploitation and post-exploitation.


3. **A fully autonomous, "War-driving Raspberry Pi". Do not confuse this one with #1.** As this Raspberry Pi's mission is to grab NEW ENCRYPTED PASSWORDS as I move from one spot to another. 

The purpose of the other Pi, is to break back into a network that we have just CRACKED credentials of. 


Both of them are powered by automation scripts that are practically "dumbed-down". In other words, it really can't do much of a job outside of what I designed them to do, but it does their assigned tasks, very very well, as long as it's plugged into a microusb cord.


What else should I mention? I also **built a wireless attack drone out of a AR Drone 2.0** I got from Fry's at Black Friday.

Also more than meets the eye for all of these Raspberry Pi's. They might look small, but they pack quite a punch. In both the initial deauth-attack and returning exploitation phases of the pentests, they are equipped with top-of-the-line wireless antennas that are extremely hard to find out in the wild.

I have four amplifiers mated to a network card at any time of the day.

	**2x Hak5 Wireless Adapters with a integrated RT3070 Wi-Fi Amplifier
	1x Hak5 Long-Range 400-to-800mW Wi-Fi Booster for reverse-SMA connections
	1x Ubiquiti Networks M2 Bullet Wireless Signal Injector**, 

with special features such as audio-beep assisted targeting, persistent-reconnections with my targets, and a neat spectrum analyzer to determine levels of interference and the feasibility of a attack angle if you consider radio interference.


	**Also 2x Antennas exceeding 13 dbi, each.**
	a. One is a SimpleWiFi 2.4Ghz Parabolic Dish Antenna with a rating of 24 dbi
	b. Another is a cheap TrendNet Panel I got from Fry's rated at 14dbi. It is still useful because it allows the signal to be projected in a 30-degree wide "cone", which is more suitable for Rogue Access Points. 


# Incident Response to a Unexpected Attack from Unknown Assailants.

Earlier this month, my website has suffered a major network attack caused by a brute-forcing botnet (of approximately 1,868 bots) that nearly killed my servers. As a response, I constructed **a automatic snort alert log parser and autobanner**, as well as custom configurations for Intrusion Prevention and Detection Systems for VPS-hosted websites.

Not only did I turn the tables on the attacker with just a few simple fail2ban and snort rules applied company-wide (and a full switch-out of every port, especially 22, to avoid attracting new dickheads), but I also managed to enumerate the HTTP headers of the attacker, causing him to be "put on the run". 

**Anyways, this is my first two days back to work since the last day of class**. I will have a long busy time building my company (and I don't think I passed the exam) but I will try my best to ensure that the more useful of my creations will trickle it's way into public release in ArmsCommander and Cylon-Raider. **My main concern is that  in particular for this update, a lot of the things it purports to do may end up breaking your system. 

It requires root-level access to everything, and it messes with critical startup processes to achieve the cyber-defense results that I wanted. For that reason, **I decided to create a "Prototyping Repo" located here, https://github.com/tanc7/ArmsCommander-TestBed. You may try them out if you wish**, but you must understand that I am not responsible for any unforseen incidents and/or damages caused by this. You are taking this, out of your own risk. Also be aware that the scripts located in that link are NOT complete. And that means little to no tech support if you screw something up.

But assuming that all goes well, I may personally vet for the script or program to be added to the official Arms-Commander Repository. 

	C.T. Lister
	Lister Unlimited Cybersecurity Solutions, LLC.
	9:55pm, November 13th.


# The FOREPLAY Update: Three Brand New Spanking Toys!

**Videos will be coming soon on how to use these new scripts and toolkits. Check back soon**

# Foreplay

*"EZ-mode, Multiplayer Armitage"*

**Tutorial**: https://raw.githubusercontent.com/tanc7/Arms-Commander/master/How-To-Videos/FOREPLAY_tutorial.webm

Prepare for the hot, steamy interaction of hacker cooperation in post exploitation. Hot.

Foreplay dramatically simplifies the launching of a Armitage Teamserver, designed to overcome common annoyances with initializing the Metasploit database (for example), conflicting ports and other nuisances  that prevent a successful launch of a multi-user Metasploit session.

It saves your preferred settings automatically so you can relaunch the teamserver by typing four capital letters, "LOAD".

Now you can all circle-jerk together in pwning a box! All of the hassles have been taken care of. Gang up on a poor bastard via Armitage!

# JKD,

*"autoretaliation glitch"*

**Tutorial not necessary**: All you have to do is run a comprehensive NMap scan on yourself.

Debuted as a proof of concept right after DEFCON, this accidental discovery gives you auto-retaliation capabilities for particularly aggressive nmap scans from the OpFor.

Push of a button, and the unintended design flaw by Rapid7 will now punish dickheads that use far too many SYN packets and HTTP requests against your IP.

A total of 30 meterpreter shells were autolaunched in the test lab!

# D-RADIUS,

*"Enterprise wifi attacker"*

**Tutorial pending**: Due to GitHub file upload restrictions (no more than 25MB and I want to save space for git cloning), I plan to break down the concepts into...
	1. Configuring the fake-RADIUS attack
	2. Starting up hostapd-wpe and freeradius-wpe, and capturing a handshake
	3. Cracking the challenge-response strings with asleap

Originally I planned to scrap this project upon learning of a similar but more fleshed out app called EAPHammer at DEFCON 2017.

However I failed to find the legit copy of EH on GitHub, and so, I decided to incorporate this script into ArmsCommander.

Dradius automates the fake access point attack and running a bogus RADIUS server, intended to trick users of WPA2-ENT and MGT networks into handing you their credentials.

Dradius is a interactive option built on top of hostapd-wpe and freeradius-wpe, simplified and tested to work. No more scouring Google for outdated How-Tos on how to attack PEAP wifi networks!

Comes with its own asleap menu to quickly crack those challenge response strings!

# Further notice of developments of AC,

*"and what could happen as the result of the Marcus Hutchins Case (WannaCry-Killer Hero, arrested at DEFCON for accusations of crimeware proliferation and sales by the FBI, verdict pending)"*

A lot of you may wonder why I keep packaging these scripts into ArmsCommander instead of distributing it as standalone modules. In truth, nearly all the tools can be run standalone with a bit of tweaking of one or two lines of code per module...

The answer is... **open source licensure and my bid to avoid criminal liability for POTENTIAL MISUSE** by downloaders of ArmsCommander. By having a single license, and a loophole created by a clause in the license, I automatically avoid criminal liability for any future incidents involving strangers and the misuse of AC.

You see, you keep it open source with a thoroughly encompassing but vague legal disclaimer, then you shouldnt have to be paying for the actions of others (black hats, wolves, etc.) that had the ability to add new features in the code and possess the capacity to use it "for evil". It was a tactic cited by the CIA before the WikiLeaks releases. It got both the CIA and NSA out of hot water, and it should work on Open-Source Projects too.

**As stated in my general license, any component, script, program, or module "touched" by ArmsCommander and its derivatives, waives me of responsibility and liability from the future actions of "malevolent jerks".**

However,

The recent federal case proceedings of a Marcus Hutchins has deeply worried me, and I am considering scaling back development of AC and related works, if not just simplying halting my involvement in the project altogether.

**The forks by GH followers will not be affected, and this repo will not be taken down**, regardless. I plan to leave it here as a persistent reminder of what happens when corporate greed and negligence gets in the way of you receiving your vital security patches.

However, I am simply considering a precaution. I am, shamelessly, pondering about my self preservation since I do have a considerable criminal record (narcotics, violent crimes) and you should too (on covering your ass).

# Real life.... less time for updates :(

I am, right now, a private contractor for front end web development with a special cybersecurity secondary role. Real life responsibilities, and the demands of my clients as well as my criminal probation is placing a serious strain on my real life.

**I have jobs lined up for a few special people, unrelated to AC, but it requires very specific disciplines**. Its what my future employers demand and require. In particular, I need a "Satellite-Guy", with a solid understanding and work experience dealing with satellite TV channels, as well as Incident Response experience to secure a datacenter related to that client.

Contact me if you are interested.

# Finally, Under-the-Hood Compatibility Updates

The required pip modules wordlist is significantly chunkier than before but the outcome is the same. Installation is only 10 seconds longer.

The reason for this is the pip freeze command, which I used to pipe a snapshot of every working required Python module that ArmsCommander needs. Something I learned in coding bootcamps just a few days ago. Thanks Adam.

In this year of 2017, with record numbers of Linux kernel regressions and incompatibilities between programming language releases, I felt this is necessary. I don't want anything to break because a bugged package is released, forcing me to go back and write a hack for it.

As an end-user, you might breath a sigh of relief if you ended up with multiple Python versions installed.

The exact version of a required module will now be auto-installed through the setup.py script and the autoInstallLinux.sh script

# The Upcoming Post-DEFCON Update: J.K.D. The Bluce-Ree Edition

# First Impressions on my first ever DEFCON and my Accidental Discovery of a "Counter-Attack System"

While I didnt present because it was my first DEFCON conference, my new friends seemed to be impressed by what I already released, in particular, Cylon Raider, and **my accidental discovery during the con, a bug in Metasploit that allows you to auto-retaliate against port scanners.** Its hard to explain how it works, but I will explain in further detail when I roll it out. For now, **enjoy this video, of the unintended perk in action**: https://drive.google.com/file/d/0B5Beow8WOgBFOGF2cVdhMmJOdk0/view?usp=sharing

You see, this being my first ever DEFCON and face-to-face introduction to "hacker culture", I confused the atmosphere of the Packet Sniffing Challenge as "the Wargames" (and there ARE "Wargames", but it's known as "CTF", and its more of a King-of-the-Hill Matchup between hackers than a "actual flag").

Apparently I was not alone (about one out of three that I asked sitting beside me thought they were "supposed to hack someone"). So, I started "prepping", stockpiling "for-sure exploits" with fast, easy-to-use, pre-generated resource scripts as well as methods I cooked up to immediately "restealth" on the same network. Now, the original intent was to develop a script that warned me about NMap scans. But after a [Alt]+[Tab] or two, I noticed that I accidentally opened up 30 shells on myself in rapid succession.

A bit of investigation showed that **Metasploit "Evil File Servers", have trouble telling the difference between a SYN-based NMap Scan** (either nmap -sS <target> or a full comprehensive scan), **from a legitimate HTTP request**. Hence, the servers will launch Meterpreter shells at ANYONE that fits the "TCP Packet Category".

And for Stuart, I will name the countering exploit in honor of you, from what you taught me and what you suggested would be a good name for it, Jeet Kun Do. I am keeping it safe and leave it as a abbreviation, as some martial arts schools may trademark their names and I do not want to get sued over free software.

# What does this JKD mean?

**Note that JKD is not restricted to nmap scans,** it will auto retaliate against any "attack" that takes the form of a SYN packet, or in general any TCP protocol that causes the listeners to perceive it as a HTTP request to a malicious file server.

**Currently I am conducting more tests but you can replicate my discovery by doing these steps**

1. **Download and run the Proof of Concept code in Python**: https://raw.githubusercontent.com/tanc7/Arms-Commander/master/JKD_poc.py

2. Run a nmap scan against 127.0.0.1 after all three autopwns have loaded, totaling 50 jobs

3. In about five minutes, once the comprehensive scan begins enumerating services, the metasploit servers "overreact" and attempts to compromise the "attacking machine" by launching meterpreter shells. On the test box, it totaled about 28 to 30 meterpreter attempts. None Landed because my machine is patched. But for a Windows user, this could be a ton of malware alert popups.

# Other updates coming your way...

During DEFCON there was a Packet Sniffing Challenge which was basically a scavenger hunt (after the first exercise, which was meant to show you the ropes on using the Aircrack-ng Suite Manually). In less than 12 hours, I managed to enumerate the hidden Access Point amidst a flood of roughly a few hundred bogus wireless routers (and dangerous MitM Evil APs) in the area. **The secret was to use airodump-ng's "--wps" function. Out of the hundreds of access points, only FIVE had the right WPS-protected services**, and only 12 or so in total had WPS-enabled throughout the four days of DEFCON.

That means, in situations where Wi-Fi signals are insanely cluttered, you need to use as many filtering options as possible to "block out the noise". These options are already available within airodump-ng by typing the "airodump-ng --help" command, but I plan to make it a selectable menu.

In a longer project, I will be bringing forth a more detailed version of the "Cylon-Raider Recon Option", now that I know its importance. I will also be applying new "under-the-hood code" that will help speed up my progress tremendously and save more lines from clutter.

Stay tuned, my loves

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

    Various adaptions and buggy code in Arms-Commander that I am trying to fix as one person

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
test email fix
test
test
github sucks

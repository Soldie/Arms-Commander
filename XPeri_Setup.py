# Experimental Installer File for installing ArmsCommander
#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
# from termcolor import colored
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

print 'Warning: Continuing with the autoinstaller will cause any previous versions of ArmsCommander to be deleted'
print 'Including your log files (all of them) in the /root/ArmsCommander/logs directory'
print 'Please make a backup beforehand'

def installer():
    print 'Git Cloning latest Repo of AC'

    # Git clone
    tmp_dir = '/tmp/'
    os.chdir(tmp_dir) # change to /tmp
    os.system('git clone https://github.com/tanc7/Arms-Commander')
    AC_Dir = tmp_dir + 'Arms-Commander'
    os.chdir(AC_Dir) # change to the new directory in /tmp/Arms-Commander

    print 'Running autoinstaller'
    # Run the autoInstaller Script
    os.system('chmod 777 autoInstallLinux.sh')
    os.system('/tmp/Arms-Commander/autoInstallLinux.sh')
    print 'Finished copying files, you should be able to run AC in two ways'
    print '1st way, double clicking the Launcher icon in your /root/Desktop directory (Kali Linux only)'
    print '2nd (preferred) way, Opening terminal and typing "ArmsCommander.py"'

    print 'Now installing two required Python modules for Python 2.7 through pip, termcolor and StringIO'
    # Install the required modules
    os.system('pip install -r /root/ArmsCommander/requiredModules.txt')
    print 'Installation complete'
    # Inform the user it has been installed

    print 'Starting ArmsCommander'
    os.system('ArmsCommander.py')
    return

def main():
    continue_question = str(raw_input("Do you wish to continue? Type 'CONTINUE': "))
    if continue_question == "CONTINUE":
        installer()
    else:
        print 'You either entered a invalid option or you did not want to CONTINUE because you wanted to backup your logs'
        print 'You can close this now'
        main()
main()

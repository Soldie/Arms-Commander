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
    try:
        print 'Git Cloning latest Repo of AC'

        # Git clone
        tmp_dir = '/tmp/'
        os.chdir(tmp_dir) # change to /tmp
        os.system('git clone https://github.com/tanc7/AC-Test-Repo')
        AC_Dir = tmp_dir + 'AC-Test-Repo'
        os.chdir(AC_Dir) # change to the new directory in /tmp/AC-Test-Repo
        os.system('git submodule init')
        os.system('git submodule update')

        print 'Running autoinstaller'
        # Run the autoInstaller Script
        os.system('chmod 777 autoInstallLinux.sh')
        os.system('/tmp/AC-Test-Repo/autoInstallLinux.sh')
        print 'Finished copying files, you should be able to run AC in two ways'
        print '1st way, double clicking the Launcher icon in your /root/Desktop directory (Kali Linux only)'
        print '2nd (preferred) way, Opening terminal and typing "ArmsCommander.py"'

        print 'Now installing two required Python modules for Python 2.7 through pip, termcolor and StringIO'
        # Install the required modules
        os.system('pip install -r /tmp/AC-Test-Repo/requiredModules.txt')
        print 'Installation complete'
        # Inform the user it has been installed

        print 'Starting ArmsCommander'
        os.system('ArmsCommander.py')
        return
        # Error-Handling Block
    except (TypeError,NameError,IndentationError):
        print TypeError,NameError,IndentationError
        print '[-] Looks like the dev has a bug in the program. Notify him and what line and file it happened in'
        print "[*] Mr. Dev is prolly masterbating to porn or something"
    except KeyboardInterrupt:
        print '[-] Received exit command, quitting'
        exit(0)
    except EOFError:
        print EOFError
        print '[-] Error end of file reached'
        print '[-] Please report this error to the dev'
    except SyntaxError:
        print SyntaxError
        print '[-] Invalid syntax was used'
    except ValueError:
        print ValueError
        print '[-] Invalid number used'
    except IOError:
        print '[-] IO Error raised'
        print IOError
        print 'Either a file is not found or disk is full'
    except MemoryError:
        print MemoryError
        print '[-] Ran out of local memory resources'
    except IndentationError:
        print IndentationError
        print '[-] Looks like the dev has a bug in the program. Notify him and what line and file it happened in'
        print "Or you can fix the whitespaces yourself if you'd like (don't mix spaces and tabs, or unindent and reindent the entire block), Mr. Dev is prolly masterbating to porn or something"


def main():
    continue_question = str(raw_input("Do you wish to continue? Type 'CONTINUE': "))
    if continue_question == "CONTINUE":
        installer()
    else:
        print 'You either entered a invalid option or you did not want to CONTINUE because you wanted to backup your logs'
        print 'You can close this now'
        main()
main()

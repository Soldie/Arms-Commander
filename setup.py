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
        os.system('git clone https://github.com/tanc7/Arms-Commander')
        AC_Dir = tmp_dir + 'Arms-Commander'
        os.chdir(AC_Dir) # change to the new directory in /tmp/Arms-Commander
        os.system('git submodule init')
        os.system('git submodule update')
        os.system('chmod 777 ./*') # modifies files permissions for critical AC files including main executable
        print 'Running autoinstaller'
        # Run the autoInstaller Script
        os.system('chmod 777 autoInstallLinux.sh')
        os.system('/tmp/Arms-Commander/autoInstallLinux.sh')
        print 'Finished copying files, you should be able to run AC in two ways'
        print '1st way, double clicking the Launcher icon in your /root/Desktop directory (Kali Linux only)'
        print '2nd (preferred) way, Opening terminal and typing "ArmsCommander.py"'

        print 'Now installing two required Python modules for Python 2.7 through pip, termcolor and StringIO'
        # Install the required modules
        os.system('pip install -r /tmp/Arms-Commander/requiredModules.txt')
        print 'Now installing required repositories from the Kali APT Repo'
        os.system('sudo apt-get update && apt-get install tsocks proxychains tor -y')
        print 'Now updating the Metasploit Framework'
        os.system('msfupdate')
        print 'Now retrieving Qodas Python Mass-HTML Mailer'
        os.chdir('/root/ArmsCommander/remoteexploits')
        os.system('git clone https://github.com/qoda/python-mailer')
        print 'Now retrieving and installing the latest version of Hashcat Utilities'
        os.chdir('/tmp')
        os.system('sudo wget https://github.com/hashcat/hashcat-utils/releases/download/v1.8/hashcat-utils-1.8.7z')
        os.system('7z x ./hashcat*')
        os.chdir('./hashcat-utils-1.8/bin')
        os.system('cp -r ./cap2hccapx.bin /usr/local/bin')
        print 'Now retrieving DarkOperator Metasploit-Plugins from GitHub'
        os.system('git clone https://github.com/darkoperator/Metasploit-Plugins')
        os.chdir('./Metasploit-Plugins')
        os.system('cp -r ./*.rb /root/.msf4/plugins')
        print 'Installation complete'
        print 'To load Metasploit-Plugins, type "load pentest" in Metasploit Console'

        # Install Cylon-Raider-Lite (Separate Repo now)
        os.chdir('/tmp')
        os.system('git clone https://github.com/tanc7/Cylon-Raider')
        os.chdir('/tmp/Cylon-Raider')
        os.system('chmod 777 ./*')
        os.system('mkdir /root/Cylon-Raider-Lite')
        os.system('cp -r ./* /root/Cylon-Raider-Lite')
        os.system('cp -r Cylon_Raider_Main.py /usr/local/bin')

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

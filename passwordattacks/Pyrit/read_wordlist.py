import os
import sys
import StringIO
from termcolor import colored
import imp
password_toolkits = imp.load_source('password_toolkits', '/root/ArmsCommander/passwordattacks/password_toolkits.py')

capture_wordlist = '/root/ArmsCommander/passwordattacks/Pyrit/wordlist'
logfile_dir = '/root/ArmsCommander/logs/Pyrit'

w = open(capture_wordlist,'r')
read_w = w.read()
buf = StringIO.StringIO(read_w)
while True:
    line = buf.readline().strip()
    if line != "":
        line = line.replace('(','\(')
        line = line.replace(')','\)')
        capture_file = line
        # run_analyze(capture_file,capture_wordlist)
        cmd_String = 'pyrit -r %s analyze' % capture_file
        print colored('[*] Now analyzing %s','yellow',attrs=['bold']) % capture_file
        os.system(cmd_String)

        # we need to also capture the stdout/stderr of the previous analyzed file, which will be outputted to a logfile

        # start the logfile, also need to export the stdout data info
        # That didnt work, using Popen and stdout arguments
        # Something in how pcap works
        logfile_basename = os.path.basename(capture_file)
        logfile_name = logfile_dir + '/' + logfile_basename + '_log' + '.txt'
        cmd_String = 'pyrit -r %s analyze >> %s' % (capture_file, logfile_name)
        os.system(cmd_String)
        print colored('Your logfile is located at %s','green',attrs=['bold']) % logfile_name
        password_toolkits.pyrit_to_csv(logfile_name)

    else:
        print colored('Analysis of capture files complete','green',attrs=['bold'])
        os.system('python /root/ArmsCommander/passwordattacks/Pyrit/Pyrit.py')

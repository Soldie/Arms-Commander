#Execute script by typing either ./autoInstallLinux.sh OR
#/root/$PATH/ExtractedDirectory/autoInstallLinux.sh OR
#/home/USER/$PATH/ExtractedDirectory/autoInstallLinux.sh

#Only works in Kali Linux
#move entire directory for ArmsCommander to /root directory
echo Removing any older versions of ArmsCommander
rm -rf /root/ArmsCommander
echo Creating a new directory for /root/ArmsCommander
mkdir /root/ArmsCommander #creates the new directory
echo Creating logfile directories
mkdir /root/ArmsCommander/payloads
mkdir /root/ArmsCommander/logs/
mkdir /root/ArmsCommander/logs/nmap
mkdir /root/ArmsCommander/logs/CornHarvester
mkdir /root/ArmsCommander/logs/multi_tool_recon
mkdir /root/ArmsCommander/logs/SQLMap
mkdir /root/ArmsCommander/logs/OWASP
mkdir /root/ArmsCommander/logs/Cylon-Raider
mkdir /root/ArmsCommander/logs/CreditCardInfo
mkdir /root/ArmsCommander/logs/ngrep
echo Copying main installation into /root/ArmsCommander
cp -r ./ /root/ArmsCommander #copies contents to the new directory
echo Copying launcher icon to Kali Desktop
cp /root/ArmsCommander/Launch\ Arms\ Commander.desktop /root/Desktop # move launcher icon to Desktop for Kali Linux Desktop DIrectory
echo Copying main launcher file to /usr/local/bin
chmod 777 ./ArmsCommander.py #makes the launcher executable
cp -r ./ArmsCommander.py /usr/local/bin #copies the main launcher into the /usr/local/bin directory, allowing someone to start AC by typing "ArmsCommander.py" in terminal
echo Installing python modules via pip
pip install -r requirements.txt # installs all required python modules
echo Main Installation Completed
echo Open a terminal and type "ArmsCommander.py" to run AC, or click the Desktop Launcher
echo To use the Pupy alternative RAT interface Python-based, Similar to Meterpreter
echo You must read the installation instructions in the README.md
echo or
echo Take a look at this How-To-Video
echo https://github.com/tanc7/Arms-Commander/blob/master/How-To-Videos/How-To-Install-Pupy.webm

chmod 777 ./ *
chmod 777 ./KaliTerminalScripts/*
echo Changed all files in directory to executable
mkdir /root/Cylon-Raider
echo Creating directory /root/Cylon-Raider
cp -r ./ /root/Cylon-Raider
echo Copying Installation
cp -r /root/ArmsCommander/wirelessattacks/Cylon-Raider/KaliTerminalScripts/* /root/
echo Finished Copying all quick-scripts into /root Directory of your NetHunter Tablet
cp -r /root/ArmsCommander/wirelessattacks/Cylon-Raider/Cylon_Raider_Main.py /usr/local/bin
echo Finished copying the Cylon Raider Main Menu into /usr/local/bin
echo Open terminal and type Cylon_Raider_Main.py to start in full Kali Installs, not NH devices

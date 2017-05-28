import os
import sys
import operator
import socket

os.system('chmod 777 ./*')
os.system('mkdir /root/Cylon-Raider-Lite')
os.system('mkdir /root/Cylon-Raider-Lite/Heavy-Raider')
os.system('mkdir /root/Cylon-Raider-Lite/logs')
os.system('mkdir /root/Cylon-Raider-Lite/logs/mana_toolkit')
os.system('mkdir /root/ArmsCommander/')
os.system('mkdir /root/ArmsCommander/logs')
os.system('mkdir /root/ArmsCommander/wirelessattacks/')
os.system('mkdir /root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/')
os.system('mkdir /root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite/logs')
os.system('mkdir /root/ArmsCommander/logs/Cylon-Raider')
os.system('cp -r ./* /root/ArmsCommander/wirelessattacks/Cylon-Raider-Lite')
os.system('cp -r ./* /root/Cylon-Raider-Lite')
os.system('cp -r Cylon_Raider_Main.py /usr/local/bin')
print '[+] Install Completed, type Cylon_Raider_Main.py in terminal to get started'

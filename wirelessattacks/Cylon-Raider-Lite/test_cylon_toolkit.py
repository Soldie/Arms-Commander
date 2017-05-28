import Cylon_Toolkit_new
import os
import sys

temp_airodump_recon_csv_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv_temp.csv'

# Cylon_Toolkit.determine_type_of_file(temp_airodump_recon_csv_file)
temp_airodump_recon_file = '/root/Cylon-Raider-Lite/logs/airodump_recon_file_csv_temp.csv'
temp_file_BSSID_targeted = '/root/Cylon-Raider-Lite/logs/temp_file_BSSID_targeted.csv'
target_number = 0

os.system('clear')
Cylon_Toolkit_new.read_temp_recon_file(temp_airodump_recon_file,target_number)

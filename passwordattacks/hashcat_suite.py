#!/usr/bin/env python
# coding=UTF-8

#The first line allows this script to be executable

import os
import socket
import operator
from termcolor import colored
import sys
# hashcat suite by Chang Tan Lister
# homemade tools deemed useful in efficiently operating hashcat

print colored('Hashcat Interactive Menu Suite by Chang Tan Lister','cyan',attrs=['bold'])

def convert_aircrack_hccapx():
    print colored('MeowMix, the mass Aircrack-to-Hashcat Format Converter','white',attrs=['bold'])
    os.system('python /root/ArmsCommander/passwordattacks/meowmix.py')
    return

def autoload_hccapx_hashcat():
    opt_List = [
        '\n\t#0. Return to Main Menu',
        '#1. Crack a wordlist of hccapx files',
        '#2. Edit the wordlist of hccapx files'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        main()
    elif opt_Choice == "1":
        os.system('python /root/ArmsCommander/passwordattacks/CocaineFactory.py')
    elif opt_Choice == "2":
        os.system('leafpad /root/ArmsCommander/passwordattacks/CocaineFactory/wordlist')
        autoload_hccapx_hashcat()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        autoload_hccapx_hashcat()
    return

def videocard_tuner():
    print colored('CUDA GPU Tuning Menu for NVIDIA System Management Interface','white',attrs=['bold'])
    os.system('python /root/ArmsCommander/passwordattacks/CUDA_Setup_Utility/CUDAcontroller.py')
    return

def dump_cracked_hashes():
    print colored('Dump Cracked Hashes from Hashcat','white',attrs=['bold'])
    os.system('python /root/ArmsCommander/passwordattacks/dumpcrackedhashes.py')
    return

def custom_hashcat():
    print colored('Inter-Cat, the interactive menu for hashcat','white',attrs=['bold'])
    os.system('python /root/ArmsCommander/passwordattacks/intercat.py')
    return

def cuda_setup_utils():
    print colored('[*] Installing CUDA Setup Utility','yellow',attrs=['bold'])
    os.system('python /root/ArmsCommander/passwordattacks/CUDA_Setup_Utility/setup.py')
    print colored('[+] Installation completed, the CUDA setup utility can be run by typing "CUDA_setup_utility.py in terminal"','green',attrs=['bold'])
    main()
    return

def pyrit_analyze():
    print colored('[*] Launching Pyrit-Analyze','yellow',attrs=['bold'])
    os.system('python /root/ArmsCommander/passwordattacks/Pyrit/Pyrit.py')
    main()

def main():
    opt_List = [
        '\n\t#0. Main Menu',
        '#1. Mass-Convert WPA2-PSK handshakes into Hashcat Format HCCAPX',
        '#2. Mass-Autoload .hccapx format files into hashcat',
        '#3. Video card tuner for NVIDIA CUDA core GPUs and GPU monitoring systems',
        '#4. Dump cracked hashes',
        '#5. Run, INTER-CAT, the interactive menu to simplify the usage of hashcat',
        '#6. Pyrit-Analyze Capture Files, check whether or not your capture files have valid EAPOL handshakes',
        '#CUDAINSTALL. Run the CUDA Setup Suite to install drivers and configure fresh NVIDIA GPU systems for password cracking'
    ]

    print ("\n\t".join(opt_List))

    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        os.system('clear')
        os.system('python /root/ArmsCommander/ArmsCommander.py')
    elif opt_Choice == "1":
        os.system('clear')
        convert_aircrack_hccapx()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        autoload_hccapx_hashcat()
        main()
    elif opt_Choice == "3":
        os.system('clear')
        videocard_tuner()
        main()
    elif opt_Choice == "4":
        os.system('clear')
        dump_cracked_hashes()
        main()
    elif opt_Choice == "5":
        os.system('clear')
        custom_hashcat()
        main()
    elif opt_Choice == "6":
        os.system('clear')
        pyrit_analyze()
        main()
    elif opt_Choice == "CUDAINSTALL" or "INSTALL":
        os.system('clear')
        cuda_setup_utils()
        main()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        main()
main()

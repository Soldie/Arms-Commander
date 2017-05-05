#Define execution policies
#!/usr/bin/env python
# coding=UTF-8

#import modules
import os
import socket
import operator
from termcolor import colored
import sys
import StringIO
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=64, cols=200)) # sets window to full screen

# Inter-Cat is the interactive menu for hashcat to easily select menu options for hashcat GPU password attacks
 #
 #  # | Mode
 # ===+======
 #  0 | Straight, regular dictionary attack
 #  1 | Combination, requires two wordlists, combines words from two wordlists to generate a new password file for attack, also called combinator attack
 #  3 | Brute-force
 #  6 | Hybrid Wordlist + Mask
 #  7 | Hybrid Mask + Wordlist

 # We need a dict for -a # to specify type of attacks
 # workload profile is set right after attack types
#
# cmd_String_Brute = "hashcat -a %s -w %s -m %s %s %s" % (attack_type, workload_profile, hash_type, charset, pw_len_range) # replaced by mask attack_type
#
# cmd_String_Straight = "hashcat -a %s -w %s -m %s %s %s" % (attack_type, workload_profile, hash_type, hash_file, dict_file)
# cmd_String_Combinator = "hashcat -a %s -m %s %s %s %s" % (attack_type, hash_type, hash_file, dict_1, dict_2)
#
# # both are attack types six and seven respectively
# cmd_String_Hybrid = "hashcat -a %s -m %s %s %s %s" % (attack_type, hash_type, hash_file, dict_file, charset) #This is really good one, combiens dictionary with brute forcing
# cmd_String_Hybrid_Reverse = "hashcat -a %s -m %s %s %s %s" % (attack_type, hash_type, hash_file, charset, dict_file)

print colored('WARNING: This portion of the password-attacks section is still in development, the dev is still learning how the hashcat syntax works','white',attrs=['bold'])

# dict_file = str(raw_input("Enter the FULL PATH to your PASSWORD DICTIONARY FILE: "))
hash_type = '2500'

# We need to add other types of hash types into a dictionary file

# the non-straight attack types should be used with a crunched wordlist.
def straight_attack():
    print colored('[*] Selected Straight/Direct Dictionary Attack','green',attrs=['bold'])
    attack_type = '0'
    # hash_type = hash_dict[hash_user_input]
    hash_file = str(raw_input("Enter the full path of the hash file: "))
    dict_file = str(raw_input("Enter the full path of the dict file: "))
    # workload_user_input = str(raw_input("Enter a OPTION: "))
    # workload_profile = workload_dict[workload_user_input]
    os.system('cat /root/ArmsCommander/passwordattacks/workload_list.txt')
    workload_profile = str(raw_input("Enter a OPTION: "))
    cmd_String_Straight = """
    hashcat -a %s -w %s -m %s '%s' '%s'
    """ % (attack_type, workload_profile, hash_type, hash_file, dict_file)
    print cmd_String_Straight
    os.system(cmd_String_Straight)
    return

def combination_attack():
    print colored('[*] Selected Combinator (2x Dictionary) Attack','yellow',attrs=['bold'])

    attack_type = '1'
    hash_file = str(raw_input("Enter the full path of the hash file: "))
    dict_1 = str(raw_input("Enter your FIRST password dictionary file: "))
    dict_2 = str(raw_input("Enter your SECOND password dictionary file: "))
    os.system('cat /root/ArmsCommander/passwordattacks/workload_list.txt')
    workload_profile = str(raw_input("Enter a OPTION: "))
    # cmd_String_Brute = "hashcat -a %s -w %s -m %s %s %s" % (attack_type, workload_profile, hash_type, charset, pw_len_range)
    cmd_String_Combinator = """
    hashcat -a %s -w %s -m %s '%s' '%s' '%s'
    """% (attack_type, workload_profile, hash_type, hash_file, dict_1, dict_2)
    print cmd_String_Combinator
    os.system(cmd_String_Combinator)
    return

def brute_attack():
    print colored('[*] Selected Mask/Brute Force Attack','red',attrs=['bold'])

    attack_type = '3'
    hash_file = str(raw_input("Enter the full path of the hash file: "))
    charset = str(raw_input("Enter the PATH of the character set you wish to attack with: "))
    pw_len_range = str(raw_input("Enter the password length range you are attacking: "))
    os.system('cat /root/ArmsCommander/passwordattacks/workload_list.txt')
    workload_profile = str(raw_input("Enter a OPTION: "))
    cmd_String_Brute = """
    hashcat -a %s -w %s -m %s '%s' %s %s
    """% (attack_type, workload_profile, hash_type, hash_file, charset, pw_len_range)
    print cmd_String_Brute
    os.system(cmd_String_Brute)
    return

def hybrid_attack():
    print colored('[*] Selected Hybrid Dictionary + Generated Attack','magenta',attrs=['bold'])

    attack_type = '6'
    hash_file = str(raw_input("Enter the full path of the hash file: "))
    dict_file = str(raw_input("Enter your password DICTIONARY FILE: "))
    charset = str(raw_input("Enter the CHARACTER SET that follows the password: "))
    os.system('cat /root/ArmsCommander/passwordattacks/workload_list.txt')
    workload_profile = str(raw_input("Enter a OPTION: "))
    cmd_String_Hybrid = """
    hashcat -a %s -w %s -m %s '%s' '%s' '%s'
    """ % (attack_type, workload_profile, hash_type, hash_file, dict_file, charset)
    print cmd_String_Hybrid
    os.system(cmd_String_Hybrid)
    return

def reverse_hybrid_attack():
    print colored('[*] Selected Reverse Hybrid Generated + Dictionary Attack','cyan',attrs=['bold'])

    attack_type = '7'
    hash_file = str(raw_input("Enter the full path of the hash file: "))
    dict_file = str(raw_input("Enter your password DICTIONARY FILE: "))
    charset = str(raw_input("Enter the CHARACTER SET that follows the password: "))
    os.system('cat /root/ArmsCommander/passwordattacks/workload_list.txt')
    workload_profile = str(raw_input("Enter a OPTION: "))
    cmd_String_Hybrid_Reverse = """
    hashcat -a %s -w %s -m %s '%s' '%s' '%s'
    """ % (attack_type, workload_profile, hash_type, hash_file, charset, dict_file)
    print cmd_String_Hybrid_Reverse
    os.system(cmd_String_Hybrid_Reverse)
    return

def dump_cracked_hashes():
    os.system('python /root/ArmsCommander/passwordattacks/dumpcrackedhashes.py')
    return
def main():
    opt_List = [
        '\n\t#0. Exit Program',
        '#1. Straight Wordlist Attack, single wordlist',
        '#2. Raw Brute Force Attack',
        '#3. Combinator Attack, use two wordlists to combine password combinations',
        '#4. Hybrid Attack',
        '#5. Reverse-Hybrid Attack',
        '#6. Dump all cracked hashes from a wordlist of HCCAPX files'
    ]

    print ("\n\t".join(opt_List))
    opt_Choice = str(raw_input("Enter a OPTION: "))

    if opt_Choice == "0":
        exit(0)
    elif opt_Choice == "1":
        os.system('clear')
        straight_attack()
        main()
    elif opt_Choice == "2":
        os.system('clear')
        brute_attack()
        main()
    elif opt_Choice == "3":
        os.system('clear')
        combination_attack()
        main()
    elif opt_Choice == "4":
        os.system('clear')
        hybrid_attack()
        main()
    elif opt_Choice == "5":
        os.system('clear')
        reverse_hybrid_attack()
        main()
    elif opt_Choice == "6":
        os.system('clear')
        dump_cracked_hashes()
        main()
    else:
        print colored('You have entered a invalid option','red',attrs=['bold'])
        main()
main()

import toolkits
import socket
import os
import sys
import operator

wordlist_file = "/root/Documents/wmv_to_mp4_converter/convert_wordlist.txt"
def install():
    cmd_str = """sudo apt-get update && apt-get install ffmpeg -y"""
    os.system(cmd_str)
    main()
    return

def edit_wordlist():
    os.chdir("/root/Documents/wmv_to_mp4_converter")
    os.system('echo "" > /root/Documents/wmv_to_mp4_converter/convert_wordlist.txt')
    os.system("leafpad convert_wordlist.txt")
    main()
    return

def run_converter():
    toolkits.video_converter(wordlist_file)
    main()
    return

def main():
    print """

    # INSTALL, install ffmpeg codecs and converters
    # EDIT, edit the wordlist of files you want to convert
    # RUN, run the converter through each file, generating a MP4 equivalen for each WMV file in the same directory
    """

    opt_choice = str(raw_input("Type a COMMAND: "))

    if opt_choice == "INSTALL":
        install()
    elif opt_choice == "EDIT":
        edit_wordlist()
    elif opt_choice == "RUN":
        run_converter()
    else:
        print toolkits.red("You have entered a invalid option")
        main()
    return
main()

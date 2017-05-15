

# this should be moved or copied over to the Wireless Attacks Menu. This is not actually reconnaissance.
def pyrit_to_csv(pyrit_analyze_output_file): # searches pyrit files for handshakes, organizes it by good, workable, or bad
# warning this is draft code. This is a parser for Pyrit output. To convert it to csv format to better organize captured handshakes .cap files
    pyrit_log_dir = ''
    pyrit_log_csv = pyrit_analyze_output_file + '_log_parsed.csv'

    r = open(pyrit_analyze_output_file,'r')
    w = open(pyrit_log_csv)

    with open(pyrit_analyze_output_file,'r') as r:
        line = r.readline()
        sentence = str(line)
        for sentence in r:
            if re.findall('Parsing file',str(sentence)):
                Capture_File = sentence
                Capture_File = Capture_File.replace("Parsing file '","")
                Capture_File = Capture_File.replace("'","")
            if re.findall('AccessPoint',str(sentence)): #1: AccessPoint 78:24:af:ed:ab:a0 ('Prettyfly4awifi'):
                Wifi_AP = sentence.split("('")
                Wifi_AP = sentence.replace('AccessPoint','')
                Wifi_MAC_BSSID = sentence[0]
                Wifi_ESSID = sentence[1]

            if re.findall('Station',str(sentence)):   #1: Station 60:6d:c7:8b:ef:20, 3 handshake(s):
                Wifi_Client = sentence.split(',')
                Wifi_Client = sentence.replace('Station','')
                Wifi_Client_MAC = sentence[0]
                Wifi_Client_Handshakes_Count = sentence[1]

            write_string = '\nESSID:,%s,BSSID:,%s,HANDSHAKES:,%s,CLIENT MAC:,%s,CAPTURE FILE:,%s' % (Wifi_ESSID, Wifi_MAC_BSSID, Wifi_Client_Handshakes_Count, Wifi_Client_MAC, Capture_File)
            w.write(write_string)
        r.close()
        w.close()
        print colored('Pyrit Analysis converted into CSV file: %s','yellow',attrs=['bold']) % pyrit_log_csv

    return

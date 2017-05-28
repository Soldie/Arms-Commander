import recon_toolkits
import re
import os, sys, socket

wordlist = '/root/Documents/ipwordlist.txt'
recon_toolkits.nmap_read_wordlist(wordlist)
# recon_toolkits.nmap_ncrack_scanner(ip_addr)

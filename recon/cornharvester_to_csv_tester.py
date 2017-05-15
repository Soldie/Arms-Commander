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
import re
import recon_toolkits

cornharvester_output_file = '/root/ArmsCommander/logs/CornHarvester/usps.gov.txt'

recon_toolkits.cornharvester_to_csv(cornharvester_output_file)

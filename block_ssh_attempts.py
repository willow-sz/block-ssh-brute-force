#!/usr/python3

import fwblock
import re

#reading out the file
searchInvalid = open('./sshdlog')

searchInvalid.readlines() 

# creating a regex pattern for IP addresses
patternForIP = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
 
# initializing the list object
lst=[]
 
# searching for the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])
 
# searhing for 'invalid user' in the sshdlog file
InvalidFound = searchInvalid.count("invalid")

#blocking ip address if there are 3 attempts
if InvalidFound == 3:
 fwblock.block_ip('172.2.0.123')

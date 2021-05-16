#!/usr/python3

import fwblock
import re

#reading file sshdlog

with open (sshdlog) as f:
 data = f.read()


for line in contents:

#searching for 'invalid user' in the text file

 if 'invalid user' in contents:
  ip = re.findall(re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"), line)
   n = contents.count(re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"))

#checking if ip appears 3 or more times, if yes, blocking it

 if n >= 3:
  fwblock.block_ip(ip)

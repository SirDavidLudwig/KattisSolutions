#!/usr/bin/python3
import re
import sys

for line in sys.stdin:
	line = line.strip()
	whitespace = len(re.findall(r'[_]', line))
	lowercase  = len(re.findall(r'[a-z]', line))
	uppercase  = len(re.findall(r'[A-Z]', line))
	symbols    = len(line)-whitespace-lowercase-uppercase
	
	print(whitespace/len(line))
	print(lowercase/len(line))
	print(uppercase/len(line))
	print(symbols/len(line))
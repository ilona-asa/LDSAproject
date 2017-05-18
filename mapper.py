#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
# each line in each file
for line in sys.stdin:
	
	Date = ""
	From = ""
	
	#So that we only read header
	while line != "\n":
		
		#remove leading and trailing whitespace
		line = line.strip()
		
		# split the line into words
		words = line.split()
    
		if "Date:" == words[0]:
			
			#Pick second word
			Date = words[1]
	
		if "From:" == words[0]:
			
			#Pick second word
			From = words[1]
			
		if Date != "" and From != "":
			print '%s\t%s' % ([From, Date], 1)
			
		
			
		

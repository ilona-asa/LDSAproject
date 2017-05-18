#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
# each line in each file
for line in sys.stdin:
	
	#So that we only read header
	while line != "\n":
		
		# remove leading and trailing whitespace
		#line = line.strip()
		
		# split the line into words
		words = line.split()
    
		if "From:" in words:
		
			#PIC SECOND WORD IN WORDS
			#print '%s\t%s' % (word, 1)
			
	    if "Date:" in words:
			
			#PICK SECOND WORD IN WORDS
			#print '%s\t%s' % (word, 1)	
		

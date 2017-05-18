#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
# each line in each file
for line in sys.stdin:
<<<<<<< HEAD
    # remove leading and trailing whitespace
#    while line != "\n":

        line = line.strip()
        # split the line into words
        words = line.split()
        #print words[0]
        if 'Date:' in words[0]:
                date_temp = words[1]
                date = date_temp[:-1]
                print date
        
        if 'From:' in words[0]:
                sender =  words[1]
                break
        

        # increase counters
        #for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # tab-delimited; the trivial word count is 1
        print '%s\t%s' % ((sender,date), 1)
=======
	
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
			
		
			
		
>>>>>>> be5fae70cd41db3b0b81fc48d2075ea36063bdb0

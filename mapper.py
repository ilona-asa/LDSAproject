#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
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

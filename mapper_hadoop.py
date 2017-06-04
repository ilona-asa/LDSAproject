#!/usr/bin/env python
import sys

for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        words = line.split()
        if words != []:
                # use Message-ID as unique identifier of 1 email
                if 'Message-ID:' in words[0]:
                        DatePossible = True
                        FromPossible = True
                        sender = None
                        date = None
                # search for date abrreviation
                if 'Date:' in words[0] and DatePossible:
                        date_temp = words[1]
                        date = date_temp[:-1]
                        DatePossible = False
                # search for sender from enron account
                if 'From:' in words[0] and FromPossible:
                        sender =  words[1]
                        FromPossible = False
                        if 'enron' in words[1]:
                                print '%s\t%s' % ((sender,date), 1)
                                

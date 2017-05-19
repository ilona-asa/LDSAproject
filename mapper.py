#!/usr/bin/env python
		
import os

rootdir ='/home/alekodu/Downloads/Large Datasets for Scientific Applications/Miniproject/enron_mail_20110402/maildir'

for user in os.listdir(rootdir):
	for sent in os.listdir(rootdir+'/'+user):
		if (sent == 'sent_items'):
			for mail in os.listdir(rootdir+'/'+user+'/'+sent):
				#print mail
				if os.path.isfile(rootdir+'/'+user+'/'+sent+'/'+mail):
					f = open(rootdir+'/'+user+'/'+sent+'/'+mail, 'r')
					#print f.readlines()
					
					for line in f:
						line = line.strip()
						# split the line into words
						words = line.split()
						#print words[0]
						if 'Date:' in words[0]:
								date_temp = words[1]
								date = date_temp[:-1]
								#print date
				
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
					f.close()

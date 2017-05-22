#!/usr/bin/env python
		
import os

rootdir ='/home/alekodu/Downloads/Large Datasets for Scientific Applications/Miniproject/enron_mail_20110402/maildir'

for user in os.listdir(rootdir):
	for sent in os.listdir(rootdir+'/'+user):
		if (sent == 'sent_items'):
                        print '%s\t%s' % ('sentFolders', 1)
			for mail in os.listdir(rootdir+'/'+user+'/'+sent):
				#print mail
				if os.path.isfile(rootdir+'/'+user+'/'+sent+'/'+mail):
					f = open(rootdir+'/'+user+'/'+sent+'/'+mail, 'r')
					#print f.readlines()
					
					for line in f:
						# remove leading and trailing whitespace
                                                line = line.strip()
                                                words = line.split()
                                                if words != []:
                                                        if 'Message-ID:' in words[0]:
                                                                DatePossible = True
                                                                FromPossible = True
                                                                sender = None
                                                                date = None
                                                                print '%s\t%s' % ('emailCount', 1)

                                                        if 'Date:' in words[0] and DatePossible:
                                                                date_temp = words[1]
                                                                date = date_temp[:-1]
                                                                DatePossible = False

                                                        if 'From:' in words[0] and FromPossible:
                                                                sender =  words[1]
                                                                FromPossible = False
                                                                if 'enron' in words[1]:
                                                                        print '%s\t%s' % ((sender,date), 1)
                                                                else:
                                                                        break
					f.close()

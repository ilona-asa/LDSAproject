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
					print f.readlines()
					f.close()

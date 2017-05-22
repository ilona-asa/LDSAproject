#!/usr/bin/env python

import os

rootdir ='enron_mail_20110402/maildir'

for user in os.listdir(rootdir):
        sent_items = 0
        sent = 0
        _sent_mail = 0
        inbox = 0
        for folder in os.listdir(rootdir+'/'+user):
#               print '%s\t%s' % ((folder, os.path.isdir(folder)), 1)
                #if os.path.isdir(folder) == True:
#                for mail in os.listdir(rootdir+'/'+user+'/'+folder):
#                       if os.path.isdir(mail) == False:
#                                print '%s\t%s' % ('total', 1)
#               print folder
                if folder == 'sent_items':
                       for mail in os.listdir(rootdir+'/'+user+'/'+folder):
                               sent_items += 1
                       print '%s,%s,%s' % (user, folder, sent_items)
                elif folder == 'sent':
                       for mail in os.listdir(rootdir+'/'+user+'/'+folder):
                               sent += 1
                       print '%s,%s,%s' % (user, folder, sent)
                elif folder == '_sent_mail':
                        for mail in os.listdir(rootdir+'/'+user+'/'+folder):
                                _sent_mail += 1
                       print '%s,%s,%s' % (user, folder, _sent_mail)
                elif folder  == 'inbox':
                        for mail in os.listdir(rootdir+'/'+user+'/'+folder):
                                inbox += 1
        print '%s,%s,%s' % (user, 'sent_items', sent_items)
        print '%s,%s,%s' % (user, 'sent', sent)
        print '%s,%s,%s' % (user, '_sent_mail', _sent_mail)
        print '%s,%s,%s' % (user, 'inbox', inbox)
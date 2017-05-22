#!/usr/bin/env python
		
import os
import glob

#IMPORTANT: Root directory to the mail below
rootdir ='/home/maildir'

i = 1

for user in os.listdir(rootdir):
	for sent in os.listdir(rootdir+'/'+user):
		if (sent == 'sent_items'):
			
			#Check file type if they are txt or not
			files = glob.glob(rootdir+'/'+user+'/'+'*.txt')

			#Open the file to write in, might have to fix path
			with open("concatEmails"+str(i)+".txt", "wb") as outfile:
			
				#Opens the files in the current folder
				for f in files:
					
					#Checks if the file is below the recomended 64 MB, if it's not, it keeps writing in it
					file_info=os.stat("concatEmails"+str(i)+".txt")
					if file_info.st_size >= 67108864:
						i += 1
						open("concatEmails"+str(i)+".txt", "wb") as outfile
					
					#Open the email and write it to the current concat file
					with open(f, "rb") as infile:
					
						outfile.write(infile.read())
					
					#If we then dare to remove the files afterwards
					#os.remove(f)
					
					



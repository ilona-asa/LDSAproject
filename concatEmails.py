#!/usr/bin/env python
		
import os
import glob

#IMPORTANT: Root directory to the mail below
rootdir ='/home/.../maildir'

i = 1

for user in os.listdir(rootdir):
	print(user)
	for sent in os.listdir(rootdir+'/'+user):
		#Select what folders to read
		if sent == 'sent_items':
			
			#Picks all the files
			files = glob.glob(rootdir+'/'+user+'/'+sent+'/*.')
			
			#Open the file to append to. They are created in the same folder as the users.
			with open(rootdir+'/'+"concatEmails"+str(i)+".txt", "a") as outfile:
			
				#Opens the files in the current folder
				for f in files:
				
					#Converts to correct file path
					fbase = os.path.basename(f)
					f = rootdir+'/'+user+'/'+sent+'/'+fbase
					
					#Open the email and write it to the current concat file
					with open(f) as infile:
						for line in infile:
							outfile.write(line)
					
					#Checks if the file is above the recomended 64 MB, if it isn't, it keeps writing in it
					#If this is too slow, we could maybe only check after each sent folder.
					file_info=os.stat(rootdir+'/'+"concatEmails"+str(i)+".txt")
					if file_info.st_size >= 67108864:
						#Otherwise create a new outfile
						i += 1

						#Seem not to be needed
						outfile.close
						
						outfile = open(rootdir+'/'+"concatEmails"+str(i)+".txt", "a")
						
					#If we then dare to remove the files afterwards
					#os.remove(f)
					
					



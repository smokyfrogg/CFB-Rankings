#Usage 
#Input: 
#		provide command line argument of 'filename', the ASCII formatted stats from 
#		the official NCAA stats page (http://web1.ncaa.org/stats/StatsSrv/rankings?sportCode=MFB&academicYear=2016)
#
#Output:
#		directory ./filename/ filled with individual stats files as 'filename''stattype'.txt
#		'stattype' is the section header from the stats files

import sys, os

#check for args
if (!check_args()):
	return
#check for correct format

#prep output folder if necessary

#iterate through each chunk, writing to new file

#close out input

#success/fail notice
return

def check_args(): 	#Checks the command line arguments, returns True if valid, False otherwise
					#Prints reason for failure if False
	if (len(sys.argv) != 2):
		print 'Incorrect number of arguments. Provide only the filename of data to be split as an argument.'
		return False
	if (os.path.isfile(argv[1])):
		return True
	return False
def check_format():
	return
def clean_output():
	return
def write_chunk():
	return
def cleanup():
	return
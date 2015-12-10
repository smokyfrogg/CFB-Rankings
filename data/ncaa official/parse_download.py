#Usage 
#Input: 
#		provide command line argument of 'filename', the ASCII formatted stats from 
#		the official NCAA stats page (http://web1.ncaa.org/stats/StatsSrv/rankings?sportCode=MFB&academicYear=2016)
#
#Output:
#		directory ./filename/ filled with individual stats files as 'filename''stattype'.txt
#		'stattype' is the section header from the stats files

import sys, os

def main():
	#check for args
	if (not check_args()):
		return
	filename = sys.argv[1]
	#check for correct format
	print check_format(filename)
	if (not check_format(filename)):
		return
	#prep output folder if necessary

	#iterate through each chunk, writing to new file

	#close out input

	#success/fail notice
	return

def check_args(): 	#Checks the command line arguments, returns True if valid, False otherwise
					#Prints reason for failure if False
	if (len(sys.argv) != 2):
		print 'Incorrect number of arguments. Provide only the filename of data to be split as an argument.'
		print 'Exiting program'
		return False
	if (os.path.isfile(sys.argv[1])):
		return True
	print 'File:', '\'' + sys.argv[1] + '\'', 'not found! Exiting program.'
	return False

def check_format(filename):	#Inputs: str filename - name of file being opened
							#Outputs: returns boolean True if valid stats file, based on the header
							#False otherwise
	file = open(filename, 'r')
	firstline = file.readline()
	while (firstline.isspace()):
		firstline = file.readline()
	print firstline
	if (firstline == 'NCAA Football\n'):
		return True
	print 'File:', '\'' + sys.argv[1] + '\'', 'in incorrect format! Exiting program.'
	return False
def clean_output():
	return
def write_chunk():
	return
def cleanup():
	return

if __name__ == "__main__":
	main()
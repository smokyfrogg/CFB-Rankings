#Usage 
#Input: 
#		provide command line argument of 'filename', the ASCII formatted stats from 
#		the official NCAA stats page (http://web1.ncaa.org/stats/StatsSrv/rankings?sportCode=MFB&academicYear=2016)
#
#Output:
#		directory ./filename/ filled with individual stats files as 'filename'_'stattype'.txt
#		'stattype' is the section header from the stats files

import sys, os, shutil

def main():
	#check for args
	print 'Checking arguments...'
	if (not check_args()):
		return
	filename = sys.argv[1]
	print 'Checking file format...'
	#check for correct format
	if (not check_format(filename)):
		return
	#prep output folder if necessary
	directoryname = os.path.splitext(filename)[0] #directory name is filename, sans extention
	if (os.path.isdir(directoryname)):
		print "Cleaning old directory,", './' + directoryname + '/...'
		clean_output(directoryname)
	os.mkdir(directoryname)
	print 'Created directory, ' + './' + directoryname + '/'
	print 'Preparing to split file...'
	#iterate through each chunk, writing to new file
	write_chunks(filename, directoryname)
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
	if (not os.path.isfile(filename)):
		print 'File', filename, 'not found! Exiting program.'
		return False
	file = open(filename, 'r')
	firstline = file.readline()
	while (firstline.isspace()): #Skips through until first text line
		firstline = file.readline()
	if (firstline == 'NCAA Football\n'):
		return True
	print 'File:', '\'' + sys.argv[1] + '\'', 'in incorrect format! Exiting program.'
	return False

def clean_output(directoryname):	#Deletes directory, 'directoryname', and all files within
									#Input: str directoryname: name of directory to delete
	if (not os.path.isdir(directoryname)):
		print 'Directory', "./" + directoryname + '/', 'not found! Nothing deleted.'
		return
	shutil.rmtree(directoryname) #removes directoryname
	print "./" + directoryname + '/', 'deleted!'
	return

def write_chunks(filename, directoryname): 
	file = open(filename, 'r')	#open file
	#iterate through all lines
	#check state, a variable determining how far into the writing process for each file
	state = 0 	#state 0 is before beginning of section/after finializing last file
	chunk = None 	#The chunk to be written to a new file, initially None
	chunkname = ''	#Filename for a given chunk
	for line in file:
		if (state == 0): #before beginning of section/after finializing last file
			if (line == 'NCAA Football\n'):
				state = 1 #continue
				continue
		elif (state == 1): #Seen 'NCAA Football', skip next line
			state = 2
			continue
		elif (state == 2): 	#Seen division, category is current line
							#First line to write to file, line also determines filename
			chunkname = directoryname + ' - ' + line.strip('\n') + '.txt'
			chunk = open(directoryname + '/' + chunkname, 'w')
			chunk.write(line)
			state = 3
			continue
		elif (state == 3):
			if (line.isspace()): #if blank line
				chunk.close()
				print "File", chunkname, "successfully written!"
				state = 0
				continue
			else:
				chunk.write(line)
				continue
	#check that chunk was closed, delete if not
	if (not chunk.closed):
		chunk.close()
		print "File", chunkname, "successfully written!"
	print 'Parsing finished! Check', directoryname + '/', 'for results!'
	return

if __name__ == "__main__":
	main()
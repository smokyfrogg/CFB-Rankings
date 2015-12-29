#Usage 
#Input: 
#		provide command line argument of 'filename', the ASCII formatted stats from 
#		the Ken Massey's stats page (http://www.masseyratings.com/data.php)
#
#Output:
#		txt file with list of teams sorted by Massey's LSR ranking method based on point differential
#		http://www.masseyratings.com/theory/massey97.pdf
# 		txt file has same directory/filename as the input, with '_ranked' added to end

import sys

def main():
	#check for args
	print 'Checking arguments...'
	if (not check_args()):
		return
	infilename = sys.argv[1]
	outfilename = os.path.splitext(filename)[0] + '_ranked.txt'
	#open file
	#create dict of team name -> data scruct (PK, list of opponent PK's, total point differential)
	#create PK -> team name dict (for retreving team names for output)
	#iterate over games, update dictionary if team not seen, add opponents to list, increment/decrement point differential
	#iterate over name -> data dict, make game matrix in accordance with Massey, point differential vector
	#solve LSR equation (invert game matrix, A-1*SD = rankings)
	#make list of (LSR solution, Team PK) tuples
	#sort LSR results
	#create output text
	#cleanup, exit
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

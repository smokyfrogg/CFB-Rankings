#Usage 
#Input: 
#		provide command line argument of 'filename', the ASCII formatted stats from 
#		the Ken Massey's stats page (http://www.masseyratings.com/data.php)
#
#Output:
#		txt file with list of teams sorted by Massey's LSR ranking method based on point differential
#		http://www.masseyratings.com/theory/massey97.pdf
# 		txt file has same directory/filename as the input, with '_ranked' added to end

import sys, string, os

def main():
	#check for args
	print 'Checking arguments...'
	if (not check_args()):
		return
	in_filename = sys.argv[1]
	out_filename = os.path.splitext(in_filename)[0] + '_ranked.txt'
	#open file
	file_in = open(in_filename, 'r')
	#create dict of team name -> data scruct (PK, list of opponent PK's, total point differential)
	team_to_data = {}
	#create PK -> team name dict (for retreving team names for output)
	pk_to_teams = {}
	#iterate over games, update dictionary if team not seen, add opponents to list, increment/decrement point differential
	for line in file_in:
		game_summary = ncaa_game_convert(line)
		team1 = game_summary.team1
		team2 = game_summary.team2
		result = game_summary.result
		if team1 not in team_to_data:
			team_pk = len(pk_to_teams)
			team = Team_Data(team_pk)
			pk_to_teams[team_pk] = team1
			team_to_data[team1] = team
		if team2 not in team_to_data:
			team_pk = len(pk_to_teams)
			team = Team_Data(team_pk)
			pk_to_teams[team_pk] = team2
			team_to_data[team2] = team
		team1_data = team_to_data[team1]
		team2_data = team_to_data[team2]
		team1_data.opponents.append(team2_data.pk)
		team2_data.opponents.append(team1_data.pk)
		team1_data.gamesplayed = team1_data.gamesplayed + 1
		team2_data.gamesplayed = team2_data.gamesplayed + 1
		if result > 0:	#team1 victory, decrement from team2's results
			team1_data.differential = team1_data.differential + result
			team2_data.differential = team2_data.differential - result
		else:	#team2 victory
			team1_data.differential = team1_data.differential - result
			team2_data.differential = team2_data.differential + result
	file_in.close()
	print pk_to_teams
	#iterate over name -> data dict, make game matrix in accordance with Massey, point differential vector
	#solve LSR equation (invert game matrix, A-1*SD = rankings)
	#make list of (LSR solution, Team PK) tuples
	#sort LSR results
	#create output text
	#cleanup, exit
	return

def ncaa_game_convert(line_in):	#input: raw data from a line of Massey's NCAA game results
								#output: Game_Summary data structure
	raw = string.split(line_in)[1:] #splits raw string into individual parts, first part is date and unnecessary
	state = 0 	#tracks how far in data we've seen; 0 is still on team1, 1 is team2
	team1 = ''
	team2 = ''
	score1 = 0
	score2 = 0
	for item in raw: #compensating for the dickass decision to deliniate with spaces instead of tabs, when team names have spaces
		if state == 0:
			try:
				score1 = int(item)
				state = 1
			except ValueError:
				if team1 == '':
					if item[0] == '@':
						item = item[1:]
					team1 = item
				else:
					team1 = team1 + ' ' + item
		else:
			try:
				score2 = int(item)
				break
			except ValueError:
				if team2 == '':
					if item[0] == '@':
						item = item[1:]
					team2 = item
				else:
					team2 = team2 + ' ' + item
	game = Game_Summary(team1, team2, score1-score2)
	return game


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

class Game_Summary():	#Structure for holding the results of a game
						#Fields:
						#team1: string, name of the home team
						#team2: string, name of away team
						#result: point differential result, positive if team1 won, negative if team2 won
	def __init__(self, team1, team2, point_differential):
		self.team1 = team1
		self.team2 = team2
		self.result = point_differential
	#TODO: __str__

class Team_Data():	#Structure to keep track of a team's data
					#Fields:
					#pk: integer, primary key for a team. Used for keeping constant indexes in matrix algebra
					#opponents: list of integers, each with PK of teams played against
					#differential: total point differential
					#gamesplayed: number of games played by this team
	def __init__(self, teamPK): #initializes team's data. Each team should have a unique PK
		self.pk = teamPK
		self.opponents = []
		self.differential = 0
		self.gamesplayed = 0

	#TODO: __STR__

	def add_game(self, opponentPK, result):	#opponentPK: integer, PK of team played against
											#result: integer, point differential of game; positive for a win,
											#		negative for a loss
		self.gamesplayed = self.gamesplayed + 1
		self.opponents.append(opponentPK)
		self.differential = self.differential + result

if __name__ == "__main__":
	main()
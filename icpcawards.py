import sys 


# get the number of teams
num_teams = int(sys.stdin.readline())
# create a set that will hold universities
uni_set = set()
# loop through the teams while there are still winners to be found
while(len(uni_set) != 12):
    # read the team info
    team = sys.stdin.readline()
    team_info = team.split()
    # if the uni has not already placed
    if(not(team_info[0] in uni_set)):
        # output the university and team name
        # add the uni name to the uni set        
        print(str(team))
        uni_set.add(team_info[0])


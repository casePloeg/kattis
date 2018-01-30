import sys


# get the number of hand and the trump suit
game_info = sys.stdin.readline()
# seperate the info
game_info = game_info.split()
# convert the number of hands to an integer
game_info[0] = int(game_info[0])
# create a variable to represent trump for the game
trump = game_info[1]
# create a variable that will keep track of the total score of the game
score = 0
# loop through the hands
for i in range(0, (4*game_info[0])):
    # read the next line
    line = sys.stdin.readline()
    # create a variable for the value of the card
    value = line[0]
    # create a variable for the suit of the card
    suit = line[1]
    
    
    # if the value is an ace
    if(value == 'A'):
        # increment the score by the 11
        score += 11
    # elif the value is a king
    elif(value == 'K'):
        score += 4
    # elif the value is a queen
    elif(value == 'Q'):
        score += 3
    # elif the value is a jack
    elif(value == 'J'):
        # if the suit of the card is trump
        if(suit == trump):
            score += 20
        # else
        else:
            score += 2
    # elif the value is a 10
    elif(value == 'T'):
        score += 10
    # elif the value is a 9
    elif(value == '9'):
        # if the suit of the card is trump
        if(suit == trump):
            score += 14
# output the score for the game
print(score)
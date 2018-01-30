import sys


# get the number of battles
n = int(sys.stdin.readline())
# create a counter for won games
won = 0
# iterate through the battles
for i in range(0, n):
    # read the battle sequence
    battle = sys.stdin.readline().replace('\n','')
    # if the sequence 'CD' does not appear in the battle then it was a win
    if(battle.count('CD') == 0):
        won += 1
# output the number of won battles
print(won)
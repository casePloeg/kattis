import sys

# create a variable for the highest total
total = 0
# create a variable to represent the person with the highest total
winner = 0
#loop through the contestants
for i in range(1, 6):
    # read the next line
    line = sys.stdin.readline()
    # split line into list
    info = line.split()
    # convert elements to integers
    for j in range(0, len(info)):
        info[j] = int(info[j])
    # sum the elments together (take out the 
    new_total = sum(info)
    # if the sum is larger then the current larger total we have a new winner
    if(new_total > total):
        total = new_total
        winner = i

# output the winner and their total
print(str(winner) + ' ' + str(total))
    
    
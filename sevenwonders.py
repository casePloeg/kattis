import sys


# get the information about about which type of cards a player has
info = sys.stdin.readline().replace('\n','')
# create a counter for 't's
t_count = 0
# create a counter for 'c's
c_count = 0
# create a counter for 'g's
g_count = 0
# iterate through the letters
for char in info:
    # increment the counters based on the current letter
    if(char == 'T'):
        t_count += 1
    elif(char == 'C'):
        c_count += 1
    elif(char == 'G'):
        g_count += 1
# create a variable for the sum of points
total = 0
# calculate points
# increment by the square of the # of t's, c's g's
total += (t_count ** 2)
total += (c_count ** 2)
total += (g_count ** 2)
# incremnet by the number of sets of 3 cards of different types
count_list = [t_count, c_count, g_count]
count_list.sort()
total += count_list[0] * 7

# output the total sum of points
print(total)
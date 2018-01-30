import sys

# average = # base hits / # at-bats
# slugging percentage # of bases / # at-bats

# at-bat can ear 0, 1, 2, 3, 4, does not include 'walk'

# get the number of at-bats
at_bats = int(sys.stdin.readline())
# create a variable to hold to slug total
slugs = 0
# get the information about each at-bat
info = sys.stdin.readline()
# split the info into a list
info_list = info.split()
# convert the strings to integers
for i in range(0, len(info_list)):
    info_list[i] = int(info_list[i])
    # if the value is negative (walk)
    if(info_list[i] == -1):
        # increment the number of at-bats by negative 1
        at_bats -= 1
    # elif the value is a valid number of bases
    elif(info_list[i] in (0, 1, 2, 3, 4)):
        # increment the slug total by the value
        slugs += info_list[i]

# calculate the average, at_bats will always be > 0, according to the question
# so there is no need to prepare for 0 division
average = slugs / at_bats
# output the average
print(average)


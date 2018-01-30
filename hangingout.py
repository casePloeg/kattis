import sys


# get info
info = sys.stdin.readline().split()
# convert elements to integers
limit = int(info[0])
events = int(info[1])
# create a counter for the number of groups denied
denied = 0
# create a variable to keep track of the number of people within the building
people = 0
# iterate through the events
for i in range(0, events):
    # read the event
    event = sys.stdin.readline().split()
    ev_type = event[0]
    num = int(event[1])
    # if the event is people entering 
    if(ev_type == 'enter'):
        # if there is room for the people increment the people counter
        if((people + num) <= limit):
            people += num
        # if there is no room increment the denied counter
        else:
            denied += 1
    # if the event is people leaving
    else:
        # decrease the people counter
        people -= num
# output the value of the denied counter
print(denied)
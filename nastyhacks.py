import sys


# get the number of lines
n = int(sys.stdin.readline())
# iterate through the lines
for i in range(0, n):
    # read the next line
    line = sys.stdin.readline()
    # split the line into a list the contains r, e, and c
    advert_info = line.split()
    # convert the info into integers
    advert_info[0] = int(advert_info[0])
    advert_info[1] = int(advert_info[1])
    advert_info[2] = int(advert_info[2])
    # calculate the expected additional profit caused by advertising
    adv_profit = advert_info[1] - advert_info[0]
    # if the profit made is more than the cost of advertising
    if(adv_profit > advert_info[2]):
        # the company should advertise
        msg = 'advertise'
    # elif the profit made is less than the cost of advertising
    elif(adv_profit < advert_info[2]):
        # the company should not advertise
        msg = 'do not advertise'
    # else (the profit is equal to the cost)
    else:
        # it does not matter whether the company advertises or not
        msg = 'does not matter'
    
    # output the verdict of whether the company should advertise or not
    print(msg)
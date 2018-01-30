import sys


# get the card labels
info = sys.stdin.readline().replace('\n','')
# create sets for all 4 of the suits
p = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'}
k = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'}
h = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'}
t = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'}
# create a counter for the label number
i = 0
# create a boolean for the keeps track of whether a duplicate is 
# found or not
dup_found = False
# iterate through the labels until the end is reached or a duplicate
# is found
while((i < len(info)) and (not dup_found)):
    # get the suit of the card
    suit = info[i]
    # if the value of the card is within it's suit's set
    if((suit == 'P') and (info[i+1:i+3] in p)):
        # remove the value from the set
        p.remove(info[i+1:i+3])
    elif((suit == 'K') and (info[i+1:i+3] in k)):
        # remove the value from the set
        k.remove(info[i+1:i+3])
    elif((suit == 'H') and (info[i+1:i+3] in h)):
        # remove the value from the set
        h.remove(info[i+1:i+3])
    elif((suit == 'T') and (info[i+1:i+3] in t)):
        # remove the value from the set
        t.remove(info[i+1:i+3])    
    # if the value is not in the set
    else:
        # stop the iteration
        dup_found = True
        # create a message to represent the error
        msg = 'GRESKA'
    i += 3
# if a duplication was found output that there was an error
if(dup_found):
    print(msg)
# if not, output the number of cards each suit is missing in the
# order of P, K, H, T
else:
    p_miss = len(p)
    k_miss = len(k)
    h_miss = len(h)
    t_miss = len(t)
    print(p_miss, k_miss, h_miss, t_miss)
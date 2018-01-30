import sys


# get the info
info = sys.stdin.readline().split()
# evaluate whether there is an odd number of switches or not
is_odd_switch = (int(info[1]) % 2 == 1)
# if the number of switches is odd
if(is_odd_switch):
    # output that it is impossible to complete the track
    print('impossible')
# if the number of switches is even
else:
    # output that it is possible to complete the track
    print('possible')
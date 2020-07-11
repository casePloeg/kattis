import math


# comparison based search has a lower bound of 
# log_2_(n), so if we less that that many times to guess,
# it is impossible to gurantee the right answer (worst case
# lower bound)
n, k = map(int, input().split())
if math.log2(n) <= k:
    print('Your wish is granted!')
else:
    print('You will become a flying monkey!')

import sys
from itertools import combinations
import bisect


case = 1
for line in sys.stdin:
    n = int(line)
    nums = [int(input()) for _ in range(n)]
    res = list(map(lambda x: x[0] + x[1], combinations(nums, 2)))
    res.sort()
    # print(res)
    m = int(input())
    print('Case ', case, ':', sep='')
    for i in range(m):
        s = int(input())
        j = bisect.bisect_left(res, s)
        if j == len(res):
            print('Closest sum to', s, 'is', str(res[j-1])+'.')
        elif j == 0:
            print('Closest sum to', s, 'is', str(res[j])+'.')
        else:
            if abs(s - res[j]) < abs(s - res[j-1]):
                print('Closest sum to', s, 'is', str(res[j])+'.')
            else:
                print('Closest sum to', s, 'is', str(res[j-1])+'.')
    case += 1 

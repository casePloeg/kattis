import sys
from collections import deque

x = 2500
sys.setrecursionlimit(x)

n = int(input())
perm = deque(map(int, input().split()))

# memo based on end, basis and cur values relative to
# an origin (all we care about is the inequalities which
# don't change whether we add or subtract)
#
# number of total configs will be O(n*n) for (end, basis) 

memo = dict()
MOD = 2**31 - 1
c = [0] 
def signs(end, basis, rest):
    c[0] += 1
    if len(rest) == 0:
        return 1
    cur = rest.popleft()
    if (end, basis) in memo:
        print(end, basis)
        return memo[(end, basis)]
    res = 0
    if end < cur < basis:
        r1 = signs(cur, basis, rest.copy()) % MOD 
        r2 = signs(end, cur, rest.copy()) %  MOD
        res = r1 + r2
    elif cur < end:
        res = signs(cur, basis, rest.copy())
    elif cur > basis:
        res = signs(end, cur, rest.copy())
    
    memo[(end, basis)] = res
    return res

end = perm.popleft()
basis = perm.popleft()
print(signs(end, basis, perm) % MOD)

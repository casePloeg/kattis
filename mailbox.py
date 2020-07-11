import math


dp = [[[-1 for x in range(101)] for y in range(101)] for z in range(11)]

def solve(left, lo, hi):
    if lo >= hi:
        return 0
    if left == 1:
        hi_sum = hi * (hi + 1)  // 2
        lo_sum = lo * (lo + 1) // 2
        return hi_sum - lo_sum

    if dp[left][lo][hi] != -1:
        return dp[left][lo][hi]
    else:
        val = math.inf
        for i in range(lo+1, hi+1):
            o1 = i + solve(left, i, hi) 
            o2 = i + solve(left-1, lo, i-1)
            val = min(val, max(o1, o2))

        dp[left][lo][hi] = val 
        
        return dp[left][lo][hi] 


n = int(input())
for _ in range(n):
    k, m = map(int, input().split())
    print(solve(k, 0, m))

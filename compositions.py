p = int(input())

dp = [[[0 for x in range(31)] for y in range(31)] for z in range(31)]
# state: dp[n][m][k] = the number of compositions for n that
# miss the set defined by m + i*k for i in 0,1,2...

# transition: first we start with the base of 2**(n-1) 
# compositions, then we take away the compositions that use
# a number we are supposed to miss

# notice that compositions at n can be built by taking
# compositions at n-1, n-2, ... and adding 1, 2, ... onto
# each composition respectively

# so we iterate through all numbers j before n
# if j is in the set, then we must take out all 
# compositions for n - j
# if j is not in the set, then we take out all 
# compositions for n - j that require a number in the set
# which is equal to 2**(n-j) - dp[n-j][m][k]

for i in range(1, 31):
    for m in range(0, 31):
        for k in range(m+1, 31):
            dp[i][m][k] = (2 ** (i - 1))
            for j in range(1, i+1):
                if (j-m) % k == 0 and j == i:
                    dp[i][m][k] -= 1
                elif (j-m) % k == 0:
                    dp[i][m][k] -= 2**(i-j-1)
                elif i != j:
                    dp[i][m][k] -= 2**(i-j-1) - dp[i-j][m][k]

for _ in range(p):
    K, n, m, k = map(int, input().split())
    print(K, dp[n][m][k])



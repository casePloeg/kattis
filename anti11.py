dp = [0 for i in range(10001)]
dp[1] = 2
dp[2] = 3
for i in range(3, 10001):
    dp[i] = (dp[i-1] + dp[i-2]) % (1000000007) 

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])


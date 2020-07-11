dp = [[0 for _ in range(8)] for _ in range(30)]
dp[0][0] = 1
dp[0][3] = 1
dp[0][6] = 1
for i in range(1,30):
    dp[i][0] = dp[i-1][7]
    dp[i][1] = dp[i-1][6]
    dp[i][2] = dp[i-1][5]
    dp[i][3] = dp[i-1][4] + dp[i-1][7]
    dp[i][4] = dp[i-1][3]
    dp[i][5] = dp[i-1][2]
    dp[i][6] = dp[i-1][1] + dp[i-1][7]
    dp[i][7] = dp[i-1][0] + dp[i-1][3] + dp[i-1][6]

n = int(input())
while n != -1:
    if 3 * n % 2 != 0:
        print(0)
    elif n == 0:
        print(1)
    else:
        print(dp[n-1][7])
    n = int(input())

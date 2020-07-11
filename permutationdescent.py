dp = [[0 for _ in range(110)] for _ in range(110)]

def get_perms():
    dp[2][0] = 1
    dp[2][1] = 1
    for i in range(3, 101):
        dp[i][0] = 1
        for j in range(1, i - 1):
            dp[i][j] = dp[i-1][j-1] * (i-j) + dp[i-1][j] * (j+1)
            dp[i][j] %= 1001113
        dp[i][i-1] = 1

get_perms()
p = int(input())
for _ in range(p):
    k, n, v = map(int, input().split())
    print(k, dp[n][v])


dp = [[[-1 for x in range(15)] for y in range(30)] for z in range(30)]


def walk(i, j, s):
    if dp[i][j][s] != -1:
        return dp[i][j][s]
    elif s == 0 and (i,j) == (14,14):
        dp[i][j][s] = 1
        return 1
    elif s == 0:
        dp[i][j][s] = 0
        return 0
    else:
        dp[i][j][s] = walk(i+1, j, s-1) + walk(i, j+1, s-1) + walk(i-1, j+1, s-1) + walk(i+1, j-1, s-1) + walk(i-1, j, s-1) + walk(i, j-1, s-1)
        return dp[i][j][s]

for i in range(15):
    walk(14, 14, i)


t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[14][14][n])

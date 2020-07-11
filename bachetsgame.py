import sys


for line in sys.stdin:
    n, m, moves = line.split(' ', 2)
    n = int(n)
    m = int(m)
    moves = list(map(int, moves.split()))
    dp = [[-1 for x in range(m+1)] for y in range(n+1)]
    for i in range(n+1):
        for j in range(m):
            if i - moves[j] == 0:
                dp[i][j] = 1
                dp[i][-1] = 1
            else:
                possible = i - moves[j] > 0
                if possible:
                    outcome = dp[i-moves[j]]
                    # if opponent can win off this move, then
                    # mark it 0 (opponent wins)
                    if outcome[-1] == 1:
                        dp[i][j] = 0 
                    else:
                        dp[i][j] = 1 
                        dp[i][-1] = 1

    w = dp[i][-1] 
    if w == 1:
        print('Stan wins')
    else:
        print('Ollie wins')

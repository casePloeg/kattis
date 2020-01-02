n, m = map(int, input().split())
while( n + m != 0):
    d_heads = []
    kn_heights = []
    for i in range(n):
        d_heads.append(int(input()))
    for i in range(m):
        kn_heights.append(int(input()))
    if n > m:
        print('Loowater is doomed!')
    else:
        d_heads.sort()
        kn_heights.sort()

        j = 0
        total_gold = 0
        success = True
        for i in range(m):
            if d_heads[j] <= kn_heights[i]:
                total_gold += kn_heights[i]
                j += 1
            # defeated all dragons!
            if j == n:
                break
        if j != n:
            print('Loowater is doomed!')
        else:
            print(total_gold)

    n, m = map(int, input().split())

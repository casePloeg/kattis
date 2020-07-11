import itertools


heights = list(map(int, input().split()))
h1 = heights[-2]
h2 = heights[-1]
heights = heights[:-2]
perms = itertools.permutations(heights)
for p in perms:
    if p[0] >= p[1] >= p[2] and sum(p[:3]) == h1 and p[3] >= p[4] >= p[5] and sum(p[3:]) == h2:
        print(' '.join([str(x) for x in p]))
        break



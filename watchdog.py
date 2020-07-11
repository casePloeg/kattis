import math


n = int(input())
for _ in range(n):
    s, h = map(int, input().split())
    hatches = [list(map(int, input().split())) for i in range(h)]
    flag = True
    loc_i = 0
    loc_j = 0
    for i in range(s):
        for j in range(s):
            if [i, j] not in hatches:
                rope = max(map(lambda x: math.hypot(x[0]-i, x[1]-j), hatches))
                min_rope = min(i, s-i, j, s-j)
                if flag and rope <= min_rope:
                    flag = False
                    loc_i, loc_j = i, j
    if flag:
        print('poodle')
    else:
        print(loc_i, loc_j)

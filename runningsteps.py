# transition:
memo = dict()


def paths(s, left, n, left_1, right_1, left_2, right_2):
    s, n = s-n, 0
    min_step = min(left_1, right_1, left_2, right_2)
    left_1 -= min_step
    left_2 -= min_step
    right_1 -= min_step
    right_2 -= min_step

    if (s, n, left, left_1, left_2, right_1, right_2) in memo:
        return memo[(s, n, left, left_1, left_2, right_1, right_2)]

    if n == s and left_1 == right_1 and left_2 == right_2 and left_1 <= left_2:
        return 1
    elif n > s:
        return 0
    else:
        if left:
            r1 = paths(s, not left, n+1, left_1 + 1, right_1, left_2, right_2)
            r2 = paths(s, not left, n+2, left_1, right_1, left_2 + 1, right_2)
        else:
            r1 = paths(s, not left, n+1, left_1, right_1 + 1, left_2, right_2)
            r2 = paths(s, not left, n+2, left_1, right_1, left_2, right_2 + 1)
        memo[(s, n, left, left_1, left_2, right_1, right_2)] =r1 + r2
        return r1 + r2
       
p = int(input())
for _ in range(p):
    k, s = map(int, input().split())
    print(k, paths(s, True, 0, 0, 0, 0, 0))

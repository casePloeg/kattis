k = int(input())
n = int(input())
time = 0
cur = k - 1
for i in range(n):
    t, ans = input().split()
    t = int(t)
    time += t
    if time >= 60 * 3 + 30:
        break
    else:
        if ans not in {'N', 'P'}:
            cur += 1
            cur %= 8
print(cur + 1)


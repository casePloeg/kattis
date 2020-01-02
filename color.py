s, c, k = map(int, input().split())
socks = [int(x) for x in input().split()]
socks.sort()
total = 0
start = 0
cur = 0
num_socks = 0
while cur < s:
    num_socks += 1
    if socks[cur] - socks[start] > k:
        start = cur
        num_socks = 1
        total += 1
    elif num_socks == c:
        start = cur + 1
        num_socks = 0
        total += 1

    if cur == s - 1 and num_socks > 0:
        total += 1
    cur += 1
print(total)
from math import ceil


n = int(input())
time = [0 for _ in range(43205)]
for i in range(n):
    d, t = map(int, input().split())
    # take off
    time[t] += 1
    # flip
    time[t-d] += 1
    # put on
    time[t-(d*2)] += 1
print(ceil(max(time) / 2))

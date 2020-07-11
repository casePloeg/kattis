from collections import defaultdict


n = int(input())
dom = [input().strip() for _ in range(n)]
kattis = [input().strip() for _ in range(n)]
freq = defaultdict(int)
for s in dom:
    freq[s] += 1
total = 0
for s in kattis:
    if freq[s] > 0:
        freq[s] -= 1
        total += 1

print(total)

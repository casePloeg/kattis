from collections import defaultdict

w = list(input())
freq = defaultdict(int)
for c in w:
    freq[c] += 1

m1, m2 = 0, 0 
s = 0
for k, v in freq.items():
    s += v
    if v > m1:
        m1, m2 = v, m1
    elif v > m2:
        m2 = v
print(s - (m1 + m2))

from collections import defaultdict
import math


m1, k = input().split()
k = int(k)
freq = defaultdict(int)
cur = ''
num = ''
for i, c in enumerate(m1):
    if c.isalpha():
        if num == '':
            freq[cur] += 1 * k
        else:
            freq[cur] += int(num) * k 
        cur = c
        num = '' 
    else:
        num += c
if num == '': 
    freq[cur] += 1 * k
else:
    freq[cur] += int(num) * k

copies = math.inf
m2 = input().strip()
freq2 = defaultdict(int)
cur = ''
num = ''
for i, c in enumerate(m2):
    if c.isalpha():
        if num == '':
            freq2[cur] += 1
        else:
            freq2[cur] += int(num) 
        cur = c
        num = '' 
    else:
        num += c
if num == '':
    freq2[cur] += 1
else:
    freq2[cur] += int(num)

freq.pop('')
freq2.pop('')

for atom, v in freq2.items():
    if atom in freq:
        copies = min(copies, freq[atom] // v)
    else:
        copies = 0
        break

print(copies)
    

from collections import deque, defaultdict


def one_off(num, primes):
    digits = list(str(num))
    potential = []
    for i in range(10):
        for j in range(4):
            if digits[j] != i:
                val = int(''.join(digits[:j] + [str(i)] + digits[j+1:]))
                if primes[val] and num != val and val > 999:
                    potential.append(val)
    return potential
            

n = int(input())
primes = [1 for _ in range(10001)]
for i in range(2,100):
    for j in range(0, 10001, i):
        if j != i:
            primes[j] = 0 

adj_list = defaultdict(list) 
for i, p in enumerate(primes):
    if p and i > 999:
        for num in one_off(i, primes):
            adj_list[num].append(i)


for _ in range(n):
    s, t = map(int, input().split())
    q = [(s, 0, (s,))]
    q = deque(q)
    visited = set()
    visited.add(s)
    valid = False
    while len(q) > 0:
        cur, total, path = q.popleft()
        if cur == t:
            print(total)
            valid = True
            break
        else:
            for v in adj_list[cur]:
                if v not in visited:
                    visited.add(v)
                    q.append((v, total+1, path + (v,)))
    if not valid:
        print('Impossible')
        

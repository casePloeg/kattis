def ishappy(m, seen):
    if m == 1:
        return True
    elif m in seen:
        return False
    else:
        seen.add(m)
        n = 0
        while m > 0:
            n += (m%10)**2
            m //=10
        return ishappy(n, seen)

primes = [1 for _ in range(10001)]
for j in range(2, 100):
    for i in range(0, 10001, j):
        if i != j:
            primes[i] = 0
primes[1] = 0
p = int(input())
for _ in range(p):
    k, m = map(int, input().split())
    seen = set()
    if primes[m] and ishappy(m, seen):
        print(k, m, 'YES')
    else:
        print(k, m, 'NO')


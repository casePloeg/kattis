msg = input().strip()
n = len(msg)
r = 1
for i in range(1, n):
    if n % i == 0 and n // i >= i:
        r = i
c = n // r

res = []
for i in range(r):
    for j in range(c):
        res.append(msg[j*r+i])
print(''.join(res))

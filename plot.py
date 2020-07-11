import math


def comb(n, i):
    return int(math.factorial(n) / (math.factorial(n-i) * math.factorial(i)) ) 

def poly(coeff, x):
    res = 0
    for i, c in enumerate(coeff):
        res += c * x**(i)
    return res


coeff = list(map(int, input().split())) 
n = coeff.pop(0) + 1

ts = [0 for _ in range(n)]
cs = [0 for _ in range(n)]
m = 6

p = [0 for _ in range(m)]
p[0] = coeff[-1]
ts[0] = coeff[-1]
coeff = coeff[::-1]

for i in range(1, n):
    pi = poly(coeff, i)
    t = pi 
    for j in range(i):
        t -= ts[j] * comb(i, j) 
    ts[i] = t 


print(' '.join([str(x) for x in ts]))
    

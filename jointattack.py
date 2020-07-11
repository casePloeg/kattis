import math 


n = int(input())
xs = list(map(int, input().split()))

def frac(i, n):
    if i == n-2:
        denom = xs[i+1]
        num = xs[i] * denom + 1
    else:
        n, d = frac(i+1, n)
        denom = n
        num = denom * xs[i] + d
    return num, denom


num, denom = frac(0, n)
g = math.gcd(num, denom)
print(num//g, denom//g, sep='/')

import math


a,b = map(int, input().split('/'))
a -= 32 * b
a = 5 * a
b = b * 9
g = math.gcd(a, b)
print(a//g, '/', b//g, sep='')


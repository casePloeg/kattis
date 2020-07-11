import math


A, N = map(float, input().split())

max_a = math.pi * (N / (2 * math.pi))**2
if max_a >= A:
    print('Diablo is happy!')
else:
    print('Need more materials!')

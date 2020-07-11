import math


v = int(input())
sa = math.inf
# can brute force to find length and width bc
# only need to search sqrt(n)  n <= 1,000,000
# so time complexity is O(n) (not bad)
for i in range(1, int(math.sqrt(v))+1):
    for j in range(1, int(math.sqrt(v))+1):
        if v % (i * j) == 0:
            # found 2 params
            l, w = i, j
            h = v // (l*w)
            new_sa = 2*w*l + 2*w*h + 2*h*l
            sa = min(sa, new_sa)

print(sa)

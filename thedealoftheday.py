import itertools
import functools


cards = list(map(int, input().split()))
k = int(input())
combs = itertools.combinations(cards, k)
total = 0
for c in combs:
    total += functools.reduce(lambda x, y: x*y, c)
print(total)


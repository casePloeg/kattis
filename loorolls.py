l, n = map(int, input().split())
k = 1
og_l = l
while l % n != 0 and l > 0 and n > 0:
    n = (n - (l%n))
    l = og_l - n
    if n > 0 and l > 0:
        k += 1
print(k)


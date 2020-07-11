n = int(input())
nums = list(map(int, input().split()))
for n in nums:
    one = False
    res = 0
    i = 0
    while n > 0:
        if n % 2 == 1 and one:
            res += 0
            one = False
        elif n % 2 == 1:
            res += 2 ** i
            one = True
        elif n % 2 == 0 and one:
            res += 2 ** i
            one = True
        elif n % 2 == 0:
            res += 0
            one = False
        i += 1
        n = n // 2
    if one:
        while i < 8:
            res += 2 ** i
            i += 1
    print(res, end=' ')
print()


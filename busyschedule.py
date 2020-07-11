# 12 hour clock sorting -> am first, hours mod 12, minutes
n = int(input())
while n != 0:
    times = [input().split() for _ in range(n)]
    times = list(map(lambda x: x[0].split(':') + [x[1]], times))
    times.sort(key=lambda x: (x[2], int(x[0]) % 12, int(x[1])))
    for t in times:
        h, m, z = t
        print(h, ':', m, ' ', z, sep='')
    print()
    n = int(input())

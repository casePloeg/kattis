import sys

n = int(input())
case = 1
for line in sys.stdin:
    m = int(line)
    v1 = [int(x) for x in input().split()]
    v2 = [int(x) for x in input().split()]
    v1.sort()
    v2.sort(reverse=True)
    scalar = 0
    for i in range(m):
        scalar += v1[i] * v2[i]

    print('Case #' + str(case) + ": " + str(scalar))
    case += 1
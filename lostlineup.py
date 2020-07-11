n = int(input())
line = [0 for i in range(n)]
line[0] = 1
between = list(map(int, input().split()))
for i in range(n-1):
    line[between[i]+1] = i + 2 
print(' '.join([str(x) for x in line]))


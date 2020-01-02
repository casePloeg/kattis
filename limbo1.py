n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    total = 1 + (l+r)*(l+r+1)//2 + r
    print(total)
n = int(input())
forecast = list(map(int, input().split()))
d = -1
temp = 50
for i in range(n-2):
    t1 = forecast[i]
    t2 = forecast[i+2]
    t = max(t1, t2)
    if t < temp:
        temp = t
        d = i
print(d + 1, temp)


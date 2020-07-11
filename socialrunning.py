n = int(input())
loc = []
for i in range(n):
    loc.append(int(input()))
dist = 10**4 * 2
for i in range(n):
    dist = min(dist, loc[i] + loc[(i+2)%n])  
print(dist)


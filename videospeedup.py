n, p, k = map(int,input().split())
intervals = list(map(int, input().split()))
t = k 
total = 0
s = 1 + (p/100*n)
intervals = [0] + intervals
while len(intervals) > 0:
    total += (t - intervals[-1]) * s
    s -= p/100
    t = intervals.pop()
print(total)


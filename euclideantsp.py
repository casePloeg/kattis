import math 



n, p, s, v = map(float, input().split())

def algo(c):
    top = n * (math.log2(n))**(c * math.sqrt(2))
    bottom = p * (10 ** 9)
    return top / bottom

def flight(c):
    return (s * (1 + (1/c))) / v

low = 0.1
high = 100
best = 0

# ternary search for the minimum of the time function
# algo + flight (simplifies to  n^c + 1/c)
while low + 1 * (10 ** -9) < high:
    mid1 = low + (high - low) / 3
    mid2 = high - (high - low) / 3
    mid1_time = algo(mid1) + flight(mid1)
    mid2_time = algo(mid2) + flight(mid2)
    if mid1_time > mid2_time:
        low = mid1
    else:
        high = mid2

print(algo(low) + flight(low), low)

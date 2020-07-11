import math


n = int(input())
days = n
printers = 1
for i in range(1, n+1):
    option = math.ceil(n/printers) + i - 1
    days = min(option, days)
    printers *= 2
print(days)


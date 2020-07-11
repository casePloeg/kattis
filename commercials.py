n, p = map(int, input().split())
max_profit = 0
cur_profit = 0
listeners = [int(x) for x in input().split()]
for l in listeners:
    if cur_profit < 0:
        cur_profit = 0
    cur_profit += l - p
    if cur_profit > max_profit:
        max_profit = cur_profit
print(max_profit)


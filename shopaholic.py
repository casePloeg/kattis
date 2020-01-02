n = int(input())
prices = [int(x) for x in input().split()]
discount = 0
prices.sort(reverse=True)
for i in range(2, n, 3):
    discount += prices[i]
print(discount)
c, k = map(int, input().split())
r = c % (10 ** k)
pay = (c // (10 ** k)) * (10 ** k)
if r >= (10 ** k) / 2:
    pay += (10 ** k)
print(pay)

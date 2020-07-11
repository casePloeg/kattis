d = int(input())
r = int(input())
t = int(input())

candles = [1]
i = 2
while candles[-1] < 2000:
    candles.append(candles[-1] + i)
    i += 1

i = 0
while True:
    ri = candles[i+d] - 6
    ti = candles[i] - 3
    if ri + ti == r + t:
        print(r - ri)
        break
    i += 1

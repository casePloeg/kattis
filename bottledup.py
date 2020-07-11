# use as many of the bigger bottles as possible
# then try to fill the next with smaller bottles
# if it doesn't work, take one bigger bottom away
# until it does work
s, v1, v2 = map(int, input().split())
n1 = s // v1
left = s % v1
while n1 > 0 and left % v2 != 0:
    n1 -= 1
    left += v1

if left % v2 != 0:
    print('Impossible')
else:
    print(n1, left // v2)

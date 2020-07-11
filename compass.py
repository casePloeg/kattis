n1 = int(input())
n2 = int(input())
d1 = (n1 - n2 + 360) % 360
d2 = (n2 - n1 + 360) % 360
if abs(d1) < abs(d2):
    print(-d1)
elif abs(d1) > abs(d2):
    print(d2)
else:
    print(abs(d1))

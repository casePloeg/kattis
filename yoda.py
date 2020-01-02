n = [int(x) for x in input()]
m = [int(x) for x in input()]

while len(n) > len(m):
    m = [0] + m

while len(m) > len(n):
    n = [0] + n

new_n = ''
new_m = ''
yoda_n = True
yoda_m = True
for i in range(len(n)):
    if n[i] > m[i]:
        new_n += str(n[i])
        yoda_n = False
    elif n[i] < m[i]:
        new_m += str(m[i])
        yoda_m = False
    else:
        new_n += str(n[i])
        new_m += str(m[i])
        yoda_n = False
        yoda_m = False
if yoda_n:
    print('YODA')
else:
    print(int(new_n))
if yoda_m:
    print('YODA')
else:
    print(int(new_m))


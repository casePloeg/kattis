n = input()
while len(n) % 3 != 0:
    n = '0' + n
res = []
for i in range(0, len(n), 3):
    digit = n[i:i+3]
    res.append(int(digit[0])*4 + int(digit[1])*2 + int(digit[2]))
print(''.join([str(x) for x in res]))
    

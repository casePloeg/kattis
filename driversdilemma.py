c, x, m = map(float, input().split())
m_p_g = []
fastest = -1
for i in range(6):
    s, f = map(float, input().split())
    t = m / s
    remaining = c / 2
    remaining -= t * x
    if m < remaining * f: 
        fastest = int(s)

if fastest > -1:
    print('YES', str(int(fastest)))
else:
    print('NO')


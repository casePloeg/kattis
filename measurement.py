n, u, _, v = input().split()
m = dict()
m['th'] = 1
m['in'] = 1000
m['ft'] = 12
m['yd'] = 3
m['ch'] = 22
m['fur'] = 10
m['mi'] = 8
m['lea'] = 3

order = ['th', 'in', 'ft', 'yd', 'ch', 'fur', 'mi', 'lea']

n = int(n)
if u == 'thou':
    u = 'th'
if u == 'inch':
    u = 'in'
if u== 'foot':
    u = 'ft'
if u== 'yard':
    u = 'yd'
if u == 'chain':
    u = 'ch'
if u == 'furlong':
    u = 'fur'
if u == 'mile':
    u = 'mi'
if u== 'league':
    u = 'lea'

if v == 'thou':
    v = 'th'
if v == 'inch':
    v = 'in'
if v== 'foot':
    v = 'ft'
if v== 'yard':
    v = 'yd'
if v == 'chain':
    v = 'ch'
if v == 'furlong':
    v = 'fur'
if v == 'mile':
    v = 'mi'
if v== 'league':
    v = 'lea'

s = order.index(u)
t = order.index(v)
if s < t:
    cur = s
    while cur < t:
        n = n / m[order[cur + 1]]
        cur += 1
elif s > t:
    cur = s
    while cur > t:
        n = n * m[order[cur]]
        cur -= 1
print(n)


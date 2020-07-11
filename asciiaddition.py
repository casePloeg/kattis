codes = dict()
codes[0] = "xxxxxx...xx...xx...xx...xx...xxxxxx"
codes["xxxxxx...xx...xx...xx...xx...xxxxxx"] = 0
codes[1] = "....x....x....x....x....x....x....x"
codes["....x....x....x....x....x....x....x"] = 1
codes[2] = "xxxxx....x....xxxxxxx....x....xxxxx"
codes["xxxxx....x....xxxxxxx....x....xxxxx"] = 2
codes[3] = "xxxxx....x....xxxxxx....x....xxxxxx"
codes["xxxxx....x....xxxxxx....x....xxxxxx"] = 3
codes[4] = "x...xx...xx...xxxxxx....x....x....x"
codes["x...xx...xx...xxxxxx....x....x....x"] = 4
codes[5] = "xxxxxx....x....xxxxx....x....xxxxxx"
codes["xxxxxx....x....xxxxx....x....xxxxxx"] = 5
codes[6] = "xxxxxx....x....xxxxxx...xx...xxxxxx"
codes["xxxxxx....x....xxxxxx...xx...xxxxxx"] = 6
codes[7] = "xxxxx....x....x....x....x....x....x"
codes["xxxxx....x....x....x....x....x....x"] = 7
codes[8] = "xxxxxx...xx...xxxxxxx...xx...xxxxxx"
codes["xxxxxx...xx...xxxxxxx...xx...xxxxxx"] = 8
codes[9] = "xxxxxx...xx...xxxxxx....x....xxxxxx"
codes["xxxxxx...xx...xxxxxx....x....xxxxxx"] = 9
codes['+'] = ".......x....x..xxxxx..x....x......."
codes[".......x....x..xxxxx..x....x......."] = '+' 
eq = [list(input()) for _ in range(7)]
a = [] 
start_b = False
b = [] 
for i in range(0, len(eq[0]), 6):
    code = ''.join([''.join(line[i:i+5]) for line in eq]) 
    code = codes[code]
    if code == '+':
        start_b = True
    elif start_b:
        b.append(code)
    elif not start_b:
        a.append(code)
a_val = 0
b_val = 0
for i, v in enumerate(reversed(a)):
    a_val += 10**i * v

for i, v in enumerate(reversed(b)):
    b_val += 10**i * v
s_val = a_val + b_val
res = [[] for _ in range(7)]
s = []
if s_val == 0:
    s = [0]
else:
    while s_val > 0:
        s.append(s_val%10)
        s_val = s_val // 10
for v in reversed(s):
    code = codes[v]
    for i in range(0, len(code), 5):
        res[i//5].append(code[i:i+5])
        res[i//5].append('.')

print('\n'.join([''.join(line[:-1]) for line in res]))


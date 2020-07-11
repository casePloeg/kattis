x = int(input())
while x != 0:
    s = input().strip()
    p = input().strip()
    c = input().strip()
    d = int((len(c) ** (3/2)) + x) % (len(c))
    m = ['' for _ in range(len(c))]
    d_c = p[s.find(c[d])]
    m[d] = d_c
    prev = d_c 
    for i in range(1, len(c)):
        cur = (d - i + len(c)) % len(c) 
        a = s.find(prev)
        res = s.find(c[cur])
        b = a ^ res
        m[cur] = p[b] 
        prev = m[cur]
    print(''.join(m))

    x = int(input())

n = int(input())
valid = True
cs = set()
for i in range(n):
    print(list(cs))
    a, c = input().split('->')
    a = a.split()
    c = c.strip()
    for u in a:
        if u not in cs:
            print(i+1)
            valid = False
            break
    cs.add(c)


if valid:
    print('correct')

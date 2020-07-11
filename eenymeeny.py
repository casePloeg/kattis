rhyme = input().split()
n = int(input())
names = []
for i in range(n):
    names.append(input())
cur = 0
t1 = []
t2 = []
even = True
while len(names) > 0:
    nxt = (cur + len(rhyme) -1) % len(names)
    if even:
        t1.append(names.pop(nxt))
    else:
        t2.append(names.pop(nxt))
    
    even = not even
    cur = nxt
    if len(names) > 0:
        cur %= len(names)

print(len(t1))
print('\n'.join(t1))
print(len(t2))
print('\n'.join(t2))


info = list(input())
init = info[0]
people = info[1:]
p1 = 0
pos = init 
for p in people:
    if pos != p:
        p1 += 1
    if p != 'U':
        p1 += 1
    pos = 'U'

p2 = 0
pos = init 
for p in people:
    if pos != p:
        p2 += 1
    if p != 'D':
        p2 += 1
    pos = 'D'

p3 = 0
pos = init 
for p in people:
    if pos != p:
        p3 += 1
    pos = p
print(p1, p2, p3, sep='\n')

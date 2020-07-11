n = int(input())
vars = input().split()
vars = list(map(lambda x: 1 if x == 'T' else 0, vars))
eq = input().split()
s = [] 
for i, c in enumerate(eq):
    if c == '+':
        a, b = s.pop(), s.pop()
        s.append(a or b)
    elif c == '*':
        a, b = s.pop(), s.pop()
        s.append(a and b)
    elif c == '-':
        a = s.pop()
        s.append(not a)
    elif c.isalpha():
        s.append(vars[ord(c) - ord('A')])
    else:
        s.append(c)
v = s.pop()
if v:
    print('T')
else:
    print('F')


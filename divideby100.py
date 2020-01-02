n = list(input())
m = list(input())
if len(n) < len(m):
    n = ['0', '.'] + ['0' for i in range(len(m)-len(n)-1)] + n
else:
    index = len(n) - len(m)
    n = n[:index+1] + ['.'] + n[index+1:]
    cur = len(n) - 1
    while n[cur] != '.':
        if n[cur] == '0':
            n.pop(cur)
        else:
            break
        cur -= 1
    if n[cur] == '.':
        n.pop(cur)
print(''.join(n))

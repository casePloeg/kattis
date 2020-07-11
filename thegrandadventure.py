def pop(s):
    if len(s) > 0:
        return True, s.pop()
    return False, None


n = int(input())
for _ in range(n):
    path = list(input())
    s = []
    for obj in path:
        valid = True
        if obj in {'$', '|', '*'}:
            s.append(obj)
        elif obj == 't':
            valid, item = pop(s) 
            valid = valid and item == '|'
        elif obj == 'j':
            valid, item = pop(s) 
            valid = valid and item == '*'
        elif obj == 'b':
            valid, item = pop(s) 
            valid = valid and item == '$'
        if not valid:
            break
    if valid and len(s) == 0:
        print('YES')
    else:
        print('NO')



password, msg = input().split()
char = dict()
for c in password:
    if c in char:
        char[c] += 1
    else:
        char[c] = 1
char_set = set(password)
order = list(password)
valid = True
for c in msg:
    if c in char_set and c == order[0]:
        char[c] -= 1
        if char[c] == 0:
            char_set.remove(c)
        order.pop(0)
    elif c in char_set:
        valid = False
        break

    if len(order) == 0:
        break
valid = valid and len(order) == 0
if valid:
    print('PASS')
else:
    print('FAIL')



def reverse_case(p):
    res = []
    for c in p:
        if c.islower():
            res.append(c.upper())
        elif c.isupper():
            res.append(c.lower())
        else:
            res.append(c)
    return ''.join(res)

s = input()
p = input()
if s == p:
    print("Yes")
elif s[0].isnumeric() and s[1:] == p:
    print("Yes")
elif s[-1].isnumeric() and s[:-1] == p:
    print("Yes")
elif s == reverse_case(p):
    print("Yes")
else:
    print("No")

def v(s):
    if s == ' ':
        return 0
    else:
        return ord(s) - ord('a') + 1

def s(v):
    if v == 0:
        return ' '
    else:
        return chr(v + ord('a') -1)

n = int(input())
for _ in range(n):
    # option, msg = input().split(maxsplit=1)
    line = input()
    option = ''
    msg = ''
    for i in range(len(line)):
        if line[i] == ' ':
            option = line[:i]
            msg = line[i+1:]
            break

    if option == 'e':
        res = [0]
        for c in msg:
            res.append(res[-1] + v(c))
        for i in range(len(res)):
            res[i] = s(res[i] % 27)
        print(''.join(res[1:]))
    elif option == 'd':
        res = []
        for c in msg:
            res.append(v(c))
        for i in range(1, len(res)):
            while res[i] < res[i-1]:
                res[i] += 27
        for i in reversed(range(1, len(res))):
            res[i] = res[i] - res[i-1]
        for i in range(len(res)):
            res[i] = s(res[i])
        print(''.join(res))


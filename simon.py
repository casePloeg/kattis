t = int(input())
for _ in range(t):
    msg = input().split()
    if len(msg) > 2 and msg[0] == 'simon' and msg[1] == 'says':
        print(' '.join(msg[2:]))
    else:
        print()


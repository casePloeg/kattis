n = int(input())
while n != 0:
    bit = ['?' for i in range(32)]
    for i in range(n):
        ins = input().split()
        if ins[0] == 'SET':
            a = int(ins[1])
            bit[a] = 1
        if ins[0] == 'CLEAR':
            a = int(ins[1])
            bit[a] = 0
        if ins[0] == 'AND':
            a = int(ins[1])
            b = int(ins[2])
            if bit[a] == 0 or bit[b] == 0:
                bit[a] = 0 
            elif bit[a] == 1 and bit[b] == 1:
                bit[a] = 1
            else:
                bit[a] = '?'
        if ins[0] == 'OR':
            # for OR, we know what the value will be if
            # we see at least one 1 bit, (lazy eval)
            a = int(ins[1])
            b = int(ins[2])
            if bit[a] == 1 or bit[b] == 1:
                bit[a] = 1 
            elif bit[a] == 0 and bit[b] == 0:
                bit[a] = 0
            else:
                bit[a] = '?'

    print(''.join([str(x) for x in bit][::-1]))
    n = int(input())


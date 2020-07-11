import itertools


def f(p, t, n, cur, options, options_table):
    p = list(p)
    if cur >= len(t) or t[cur] == -1:
        return 0
    else:
        p.append(t[cur])
        if len(p) == n:
            return 1
        else:
            options = sorted(options) 
            options.append(cur*2)
            options.append(cur*2 + 1)
            options = tuple(options)
            length = len(options)
            if options in options_table:
                return options_table[options]
            count = 0
            for i, o in enumerate(options):
                rest = tuple(x for x in options if x != o)
                count += f(tuple(p), t, n, o, tuple(rest), options_table)
            option_table[tuple(options)] = count
            return count 

n = int(input())
while n != 0:
    nodes = list(map(int, input().split()))
    tree = [-1 for x in range(2**(n))]
    cur = 1
    for v in nodes:
        while tree[cur] != -1:
            if v >= tree[cur]:
                cur = cur * 2 + 1
            else:
                cur = cur * 2

        tree[cur] = v
        cur = 1
    tree = tuple(tree)
    option_table = dict()
    print(f(tuple(), tree, n, 1, tuple(), option_table))
    n = int(input())
        

import sys

vars = dict()
for line in sys.stdin:
    line = line.split()
    if line[0] == 'define':
        vars[line[2]] = int(line[1])
    else:
        if line[1] not in vars or line[3] not in vars:
            print('undefined')
        else:
            res = False
            if line[2] == '>':
                res = (vars[line[1]] > vars[line[3]])
            if line[2] == '<':
                res = (vars[line[1]] < vars[line[3]])
            if line[2] == '=':
                res = (vars[line[1]] == vars[line[3]])
            if res:
                print('true')
            else:
                print('false')

def move(instruction, x, y, d):
    if instruction == 'Left':
        d -= 1
        d += 4
        d %= 4
    elif instruction == 'Right':
        d += 1
        d %= 4
    else:
        if d == 0:
            y += 1
        elif d == 1:
            x += 1
        elif d == 2:
            y -= 1
        elif d == 3:
            x -= 1
    return d, x, y 

x, y = map(int, input().split())
n = int(input())
instruct = [input().strip() for _ in range(n)]
for i in range(n):
    t1_x, t1_y = 0, 0
    t1_dir = 0
    t2_x, t2_y = 0, 0
    t2_dir = 0
    o1 = ''
    o2 = ''

    for j in range(n):
        if j == i:
            options = {'Forward', 'Right', 'Left'}
            options.remove(instruct[j])
            o1 = options.pop()
            o2 = options.pop()
            t1_dir, t1_x, t1_y = move(o1, t1_x, t1_y, t1_dir)
            t2_dir, t2_x, t2_y = move(o2, t2_x, t2_y, t2_dir)
        else:
            o = instruct[j]
            t1_dir, t1_x, t1_y = move(o, t1_x, t1_y, t1_dir)
            t2_dir, t2_x, t2_y = move(o, t2_x, t2_y, t2_dir)

    if (t1_x,t1_y) == (x,y):
        print(i+1, o1)
        break
    elif (t2_x,t2_y) == (x,y):
        print(i+1, o2)
        break


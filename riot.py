import sys
def challenge1():
    w, h = map(int, input().split(sep=','))
    garden = [['B' for j in range(w)] for i in range(h)]
    ivy_pts = set()
    for line in sys.stdin:
        data = line.strip().split(',')
        type = data[0]

        i = data[1]
        j = data[2]
        i = int(i)
        j = int(j)
        if type == 'I':
            ivy_pts.add((j,i))
        garden[j][i] = type
    return ('\n'.join([''.join(i) for i in garden]), w, h, ivy_pts)

def flood(today, ivy_pts):
    h = len(today)
    w = len(today[0])
    tmrw = [[z for z in row] for row in today]
    tmrw_ivy_pts = set()
    valid = True
    while len(ivy_pts) > 0:
        i, j = ivy_pts.pop()
        tmrw_ivy_pts.add((i,j))
        if i > 0 and tmrw[i-1][j] == 'B':
            tmrw[i-1][j] = 'I'
            tmrw_ivy_pts.add((i-1,j))
        elif i > 0 and tmrw[i-1][j] == 'F':
            valid = False
            break
        if i < h-1 and tmrw[i+1][j] == 'B':
            tmrw[i+1][j] = 'I'
            tmrw_ivy_pts.add((i+1,j))
        elif i < h-1 and  tmrw[i+1][j] == 'F':
            valid = False
            break
        if j > 0 and tmrw[i][j-1] == 'B':
            tmrw[i][j-1] = 'I'
            tmrw_ivy_pts.add((i,j-1))
        elif j > 0 and tmrw[i][j-1] == 'F':
            valid = False
            break
        if j < w-1 and tmrw[i][j+1] == 'B':
            tmrw[i][j+1] = 'I'
            tmrw_ivy_pts.add((i,j+1))
        elif j < w-1 and tmrw[i][j+1] == 'F':
            valid = False
            break
    return (valid, tmrw, tmrw_ivy_pts)

def challenge4():
    garden, w, h, ivy_pts = challenge1()
    garden_map = garden.split('\n')
    today = [list(g) for g in garden_map]
    valid = True
    days = 0
    while valid:
        valid, tmrw, ivy_pts = flood(today, ivy_pts)
        if valid:
            today = tmrw
            days += 1
    print(days)
    print('\n'.join([''.join(i) for i in today]))


def count_flowers(i, j, garden):
    h = len(garden)
    w = len(garden[0])
    count = 0
    row = garden[i]
    col = [row[j] for row in garden]
    for z in range(j-1, -1, -1):
        if garden[i][z] == 'F':
            count += 1
        elif garden[i][z] == 'W':
            break
    for z in range(i-1, -1, -1):
        if garden[z][j] == 'F':
            count += 1
        elif garden[z][j] == 'W':
            break
    for z in range(j+1, w):
        if garden[i][z] == 'F':
            count += 1
        elif garden[i][z] == 'W':
            break
    for z in range(i+1, h):
        if garden[z][j] == 'F':
            count += 1
        elif garden[z][j] == 'W':
            break
    return count


def challenge2():
    garden, w, h,line = challenge1()
    garden_map = garden.split('\n')
    garden_map = [list(g) for g in garden_map]
    most_flowers = 0
    flower_positions = [[1 if garden_map[j][i] == 'B' else 0 for i in range(w)] for j in range(h)]
    for i in range(h):
        for j in range(w):
            if garden_map[i][j] == 'B':
                count = count_flowers(i, j, garden_map)
                if count > most_flowers:
                    most_flowers = count
                    flower_positions = [[0 for z in range(w)] for x in range(h)]
                    flower_positions[i][j] = 1
                elif count == most_flowers:
                    flower_positions[i][j] = 1
    for i in range(h):
        for j in range(w):
            if flower_positions[i][j] == 1:
                garden_map[i][j] = '*'

    return '\n'.join([''.join(i) for i in garden_map])


def challenge3():
    garden, w, h, extra_line = challenge1()
    garden_map = garden.split('\n')
    garden_map = [list(g) for g in garden_map]
    stack = []
    if extra_line != '':
        data = extra_line.strip().split(',')
        action = data[0]
        type = data[1]
        j = int(data[2])
        i = int(data[3])
        if action == 'Pick up':
            if garden_map[i][j] == type and type in {'F', 'C', 'E', 'D'}:
                stack.append(garden_map[i][j])
                garden_map[i][j] = 'B'
            else:
                return (False, garden_map)
        elif action == 'Plant':
            if len(stack) > 0 and stack[-1] == type and garden_map[i][j] == 'B':
                garden_map[i][j] = stack.pop()
            else:
                return (False, garden_map)
    for line in sys.stdin:
        data = line.strip().split(',')
        action = data[0]
        type = data[1]
        j = int(data[2])
        i = int(data[3])
        if action == 'Pick up':
            if garden_map[i][j] == type and type in {'F', 'C', 'E', 'D'}:
                stack.append(garden_map[i][j])
                garden_map[i][j] = 'B'
            else:
                return (False, garden_map)
        elif action == 'Plant':
            if len(stack) > 0 and stack[-1] == type and garden_map[i][j] == 'B':
                garden_map[i][j] = stack.pop()
            else:
                return (False, garden_map)
    if len(stack) > 0:
        return (False, garden_map)
    else:
        return (True, garden_map)

# print(challenge2())
# valid, garden = challenge3()
# if valid:
#     print('true')
# else:
#     print('false')
# print('\n'.join([''.join(i) for i in garden]))
challenge4()
c = int(input())
for z in range(c):
    # number of towns, town where the office is
    n, t = map(int, input().split())
    # employees
    e = int(input())
    # home town, num of passengers 0 == cant drive
    employees = []
    for i in range(e):
        employees.append([int(x) for x in input().split()])

    employees.sort(reverse=True, key=lambda a: a[1])
    cur_town = -1
    prev_town = -1
    capacity = 0
    commuters = [0 for i in range(n)]
    capacity = [0 for i in range(n)]
    cars = [0 for i in range(n)]
    # calculate commuters
    for i in range(e):
        if employees[i][0] == t:
            continue
        commuters[employees[i][0]-1] += 1
    possible = True
    for i in range(e):
        if capacity[employees[i][0] - 1] < commuters[employees[i][0] - 1]:
            capacity[employees[i][0]-1] += employees[i][1]
            cars[employees[i][0]-1] += 1
    for i in range(n):
        if capacity[i] < commuters[i]:
            possible = False
            break
    if possible:
        print('Case #' + str(z+1) + ':', ' '.join([str(x) for x in cars]))
    else:
        print('Case #' + str(z+1) + ':', 'IMPOSSIBLE')

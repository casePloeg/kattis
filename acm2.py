n, p = map(int, input().split())
problems = [int(x) for x in input().split()]
time = 300
points = 0
solved = 1
if problems[p] <= 300:
    points += problems[p]
    time -= problems[p]
    problems.pop(p)

    problems.sort()

    for i in range(n-1):
        if problems[i] <= time:
            time -= problems[i]
            points += 300 - time
            solved += 1
        else:
            break
    print(solved, points)
else:
    print(0, 0)
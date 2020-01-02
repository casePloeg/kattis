n = int(input())
rooms = [int(x) for x in input().split()]
total_students = sum(rooms)
info = []
for i in range(n):
    info.append([rooms[i], i])
info.sort(reverse=True, key=lambda a: a[0])
possible = True
for i in range(n):
    if total_students - info[i][0] < info[i][0]:
        possible = False
        break
if possible:
    print(' '.join([str(i[1]+1) for i in info]))
else:
    print('impossible')

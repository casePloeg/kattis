n, k = map(int, input().split())
intervals = []
for i in range(n):
    intervals.append([int(x) for x in input().split()])
intervals.sort(key=lambda a: a[1])

room_queue = []
acts = 0
booked = []
for i in range(n):
    possible = True
    hours = [0] * (intervals[i][1] + 1 - intervals[i][0])
    for j in range(len(booked) - 1, -1, -1):
        if not possible:
            break
        if booked[j][1] >= intervals[i][0]:
            if booked[j][0] >= intervals[i][0]:
                for z in range(booked[j][0] - intervals[i][0], booked[j][1] + 1 - intervals[i][0]):
                    hours[z] += 1
                    if hours[z] == k:
                        possible = False
                        break
            else:
                for z in range(booked[j][1] + 1 - intervals[i][0]):
                    hours[z] += 1
                    if hours[z] == k:
                        possible = False
                        break

    if possible:
        acts += 1

        booked.append(intervals[i])

print(acts)
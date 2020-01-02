import random


def classroom1(invs):
    intervals = invs
    intervals.sort(key=lambda a: a[1])
    room_queue = []
    acts = 0
    booked = []
    not_booked = []
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
        else:
            not_booked.append(intervals[i])
    print(sorted(not_booked))
    return acts


def classroom2(invs):
    intervals = [[] for x in range(k)]
    # sort by start time
    invs.sort(key=lambda a: (a[1], a[0]), reverse=True)
    total = 0
    i = n - 1
    while i > -1:
        added = False
        best_interval = (-1, 0)
        for j in range(k):
            if len(intervals[j]) > 0:
                if best_interval[1] < intervals[j][-1][1] and intervals[j][-1][1] < invs[i][0]:
                    best_interval = (j, intervals[j][-1][1])
                    added = True
            else:
                if best_interval[1] <= 0:
                    best_interval = (j, 0)
                    added = True
        if added:
            intervals[best_interval[0]].append(invs[i])
            invs.pop(i)
            total += 1
        i -= 1
    return total


while True:
    n = random.randint(1, 100)
    k = random.randint(1, 100)
    # n, k = 57, 3
    # invs1 = [[17, 25], [19, 31], [12, 77], [50, 83], [57, 90], [33, 54], [57, 76], [92, 96], [36, 42], [80, 85], [30, 48], [14, 38], [58, 96], [40, 53], [79, 87], [69, 84], [64, 81], [13, 54], [30, 36], [3, 95], [42, 83], [90, 90], [73, 100], [76, 96], [11, 97], [88, 96], [30, 80], [82, 90], [15, 39], [75, 93], [13, 90], [84, 91], [8, 33], [34, 38], [34, 65], [61, 72], [9, 93], [3, 68], [49, 59], [43, 45], [91, 92], [72, 86], [62, 93], [27, 48], [59, 75], [48, 94], [18, 23], [28, 83], [94, 96], [6, 46], [45, 50], [52, 63], [90, 95], [54, 57], [3, 16], [3, 33], [31, 82]]
    # invs2 = [[17, 25], [19, 31], [12, 77], [50, 83], [57, 90], [33, 54], [57, 76], [92, 96], [36, 42], [80, 85], [30, 48], [14, 38], [58, 96], [40, 53], [79, 87], [69, 84], [64, 81], [13, 54], [30, 36], [3, 95], [42, 83], [90, 90], [73, 100], [76, 96], [11, 97], [88, 96], [30, 80], [82, 90], [15, 39], [75, 93], [13, 90], [84, 91], [8, 33], [34, 38], [34, 65], [61, 72], [9, 93], [3, 68], [49, 59], [43, 45], [91, 92], [72, 86], [62, 93], [27, 48], [59, 75], [48, 94], [18, 23], [28, 83], [94, 96], [6, 46], [45, 50], [52, 63], [90, 95], [54, 57], [3, 16], [3, 33], [31, 82]]
    # invs = [[17, 25], [19, 31], [12, 77], [50, 83], [57, 90], [33, 54], [57, 76], [92, 96], [36, 42], [80, 85], [30, 48], [14, 38], [58, 96], [40, 53], [79, 87], [69, 84], [64, 81], [13, 54], [30, 36], [3, 95], [42, 83], [90, 90], [73, 100], [76, 96], [11, 97], [88, 96], [30, 80], [82, 90], [15, 39], [75, 93], [13, 90], [84, 91], [8, 33], [34, 38], [34, 65], [61, 72], [9, 93], [3, 68], [49, 59], [43, 45], [91, 92], [72, 86], [62, 93], [27, 48], [59, 75], [48, 94], [18, 23], [28, 83], [94, 96], [6, 46], [45, 50], [52, 63], [90, 95], [54, 57], [3, 16], [3, 33], [31, 82]]
    invs = []
    invs1 = []
    invs2 = []
    for i in range(n):
        s = random.randint(1, 100)
        f = random.randint(s, 100)
        invs1.append([s, f])
        invs2.append([s, f])
        invs.append([s, f])
    #
    # n, k = 4, 2
    # invs1 = [[1,4],[2,9],[4,7],[5,8]]
    # invs2 = [[1,4],[2,9],[4,7],[5,8]]
    # invs = [[1,4],[2,9],[4,7],[5,8]]

    c1 = classroom1(invs1)
    c2 = classroom2(invs2)
    print(n, k, invs, c1, c2)
    if c1 != c2:
        break

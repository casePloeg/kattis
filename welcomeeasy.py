def get_next(cur, target, i, line):
    if cur == len(target):
        return 1
    else:
        count = 0
        for j in range(i, len(line)):
            if line[j] == target[cur]:
                count += get_next(cur+1, target, j+1, line)
        return count % 10000

target = 'welcome to code jam'
n = int(input())
for _ in range(n):
    cur = 0
    line = input().strip()
    i = 0
    jam = get_next(cur, target, i, line)
    print('Case #{:d}: {:04d}'.format(_+1, jam))


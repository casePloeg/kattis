n = int(input())
tops = 0
sides = 0
for i in range(n):
    pieces = list(map(int, list(input())))
    tops += 2 - pieces[0] - pieces[1]
    sides += 2 - pieces[2] - pieces[3]
print(min(tops, sides) // 2, tops - min(tops, sides) // 2 * 2, sides - min(tops, sides) // 2 * 2)


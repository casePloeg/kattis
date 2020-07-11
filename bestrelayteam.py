def get_top3(players):
    return sum(map(lambda x: x[1], players[:3]))


def swap(team, o, first):
    for i in range(3):
        if team[i][1] - o < team[i][0] - first[0]:
            return i
    return -1


n = int(input())
team = []
players = []
for _ in range(n):
    name, first, other = input().split()
    first = float(first)
    other = float(other)
    players.append((first, other, name))
team = []
best = 1000
for i, p in enumerate(players):
    f, o, name = p
    others = sorted(players[:i] + players[i+1:], key=lambda x: x[1])
    if best > f + get_top3(others):
        best  = f + get_top3(others)
        team = [p] + others[:3]
print(best)
for i in range(4):
    print(team[i][2])


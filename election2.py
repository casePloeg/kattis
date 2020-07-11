from collections import defaultdict


n = int(input())
parties = dict()
for i in range(n):
    name = input().strip()
    party = input().strip()
    parties[name] = party

m = int(input())
votes = defaultdict(int)
for i in range(m):
    name = input().strip()
    if name in parties:
        votes[name] += 1
tie = True 
winner = ''
max_v = -1
for name, v in votes.items():
    if v > max_v:
        max_v = v
        tie = False
        winner = parties[name]
    elif v == max_v:
        tie = True

if not tie:
    print(winner)
else:
    print('tie')



from collections import defaultdict

m = int(input())
user_freq = defaultdict(set)
word_freq = defaultdict(int)
users = set()
for i in range(m):
    line = input().split()
    users.add(line[0])
    for w in line[1:]:
        user_freq[w].add(line[0])
        word_freq[w] += 1

res = []
for k,v in word_freq.items():
    if len(user_freq[k]) == len(users):
        res.append((v, k))
res.sort(key=lambda x: (-x[0], x[1]))
if len(res) == 0:
    print("ALL CLEAR")
else:
    for i in range(len(res)):
        print(res[i][1])


from collections import defaultdict

n = int(input())
songs = defaultdict(set)
e = int(input())
for i in range(e):
    ppl = input().split()
    ppl = set(ppl[1:])
    # new song
    if '1' in ppl:
        for p in ppl:
            songs[int(p)].add(i)
    else:
        # share songs
        master = set()
        for p in ppl:
            master |= songs[int(p)]
        for p in ppl:
            songs[int(p)] |= master 

for k, v in sorted(songs.items()):
    if v == songs[1]:
        print(k)

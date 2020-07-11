notes = dict()
notes['c'] = {2,3,4,7,8,9,10}
notes['d'] = {2,3,4,7,8,9}
notes['e'] = {2,3,4,7,8}
notes['f'] = {2,3,4,7}
notes['g'] = {2,3,4}
notes['a'] = {2,3}
notes['b'] = {2}
notes['C'] = {3}
notes['D'] = {1,2,3,4,7,8,9}
notes['E'] = {1,2,3,4,7,8}
notes['F'] = {1,2,3,4,7}
notes['G'] = {1,2,3,4}
notes['A'] = {1,2,3}
notes['B'] = {1,2}

t = int(input())
for _ in range(t):
    song = input().strip()
    presses = [0 for i in range(10)]
    prev = set() 
    for i in range(len(song)):
        cur = notes[song[i]]
        for f in cur:
            if f not in prev:
                presses[f-1] += 1
        prev = cur
    print(' '.join([str(x) for x in presses]))


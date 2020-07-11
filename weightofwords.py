l, w = map(int, input().split())
if 1 <= w / l <= 26: 
    res = [(w//l) for i in range(l)]
    for i in range(w % l):
        res[i] += 1

    print(res)
    print(''.join(list(map(lambda x: chr(x-1 + ord('a')), res))))
else:
    print('impossible')

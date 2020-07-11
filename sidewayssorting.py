r, c = map(int, input().split())
while r + c != 0:
    words = [list(input()) for _ in range(r)]
    flipped = list(zip(*words))
    f_words = []
    for w in flipped:
        f_words.append(''.join(w))
    f_words.sort(key=lambda x: x.lower())
    words = [list(x) for x in f_words]
    flipped = list(zip(*words))
    print('\n'.join([''.join(x) for x in flipped]))
    r, c = map(int, input().split())

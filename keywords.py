n = int(input())
keywords = set()
for i in range(n):
    w = input().lower().strip()
    w = list(w)
    for j, c in enumerate(w):
        if c == '-':
            w[j] = ' '

    keywords.add(''.join(w))
print(len(keywords))

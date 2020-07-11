t = int(input())
for i in range(t):
    want = input().strip()
    w = input().strip()
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    presses = 51 
    for i, s in enumerate([w, s1, s2, s3]):
        p = 0
        for j, c in enumerate(want):
            if j < len(s) and c != s[j]:
                p += (min(len(want), len(s)) - j) * 2
                break
        p += abs(len(want) - len(s))
        if i > 0:
            p += 1
        presses = min(presses, p)
    print(presses)



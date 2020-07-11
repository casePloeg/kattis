t = int(input())

for _ in range(t):
    n, e = map(int, input().split())
    p, q = 0, 0
    flag = False
    # find prime factors
    # brute force
    for i in range(2, n): 
        if n % i == 0:
            p, q = i, n // i 
            flag = True
            break
        if flag:
            break
    c = (p-1) * (q - 1)
    cong = 1 % c
    i = c + cong 
    d = 0
    # find d by checking appropriate values for de by
    # maintaining congruence with c
    while True:
        if i % e == 0:
            d = i // e
            break
        i += c
    print(d)


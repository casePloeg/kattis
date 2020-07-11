n = int(input())
for i in range(n):
    w = input()
    size = len(w)
    for j in range(size):
        #print((w[:j+1] * size * (j+1)))
        if (w[:j+1] * size * (j+1)).startswith(w):
            print(j+1)
            break


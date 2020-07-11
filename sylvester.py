def get_val(i, j, n):
    if n == 1:
        return 1
    else:
        if i >= n//2 and j >= n//2:
            return -1 * get_val(i-n//2, j-n//2, n//2)
        elif i >= n//2 and j < n//2:
            return get_val(i-n//2, j, n//2)
        elif i < n//2 and j >= n//2:
            return get_val(i, j-n//2, n//2)
        elif i < n//2 and j < n//2:
            return get_val(i, j, n//2)
        
t = int(input())
for _ in range(t):
    n, x, y, w, h = map(int, input().split())
    for i in range(y, y+h):
        for j in range(x, x+w):
            print(get_val(i, j, n), end=' ')
        print()
    print()



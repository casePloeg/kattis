b, d, c, l = map(int, input().split())
valid = False 
for i in range(0, l//b+1):
    for j in range(0, l//d+1):
        for k in range(0, l//c+1):
            if i * b + j * d + k * c == l:
                print(i, j, k)
                valid = True                
if not valid:
    print('impossible')

h, sep, path  = input().partition(' ')
h = int(h)
total = 2 ** (h+1)
path_val = 1
for p in path:
    if p == 'L':
        path_val *= 2
    elif p == 'R':
        path_val *= 2 
        path_val += 1
print(total - path_val)

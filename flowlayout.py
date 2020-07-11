m = int(input())
while m != 0:
    w, h = map(int, input().split())
    old_height, max_height, cur_width = 0, 0, 0
    max_width = 0
    while (w,h) != (-1,-1):
        if cur_width + w <= m:
            cur_width += w
        else:
            old_height = max_height
            cur_width = w
        max_width = max(max_width, cur_width)
        max_height = max(max_height, old_height + h)
        w, h = map(int, input().split())
    print(max_width, 'x',  max_height)
        
    m = int(input())

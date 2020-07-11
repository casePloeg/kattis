n = int(input())
while n != 0:
    boxes = []
    for i in range(n):
        boxes.append(input().split())
    m = int(input())
    for i in range(m):
        p = input().split()
        x = float(p[0])
        y = float(p[1])
        size = p[2]
        floor = True
        for j in range(n):
            x1, y1, x2, y2 = map(float, boxes[j][:4])
            s = boxes[j][4]
            if x1 <= x <= x2 and y1 <= y <= y2:
                floor = False
                if size == s:
                    print(size, 'correct')
                else:
                    print(size, s)
        if floor:
            print(size, 'floor')
    n = int(input())
    if n !=0:
        print()

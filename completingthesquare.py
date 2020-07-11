x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
dx1 = x1-x2
dy1 = y1-y2
dx2 = x1-x3
dy2 = y1-y3
dx3 = x2-x3
dy3 = y2-y3
if abs(dx1) == abs(dy2) and abs(dy1) == abs(dx2):
    p_x = x3 + dx1
    p_y = y3 + dy1
    if abs(x2 - p_x) == abs(y3 - p_y) and abs(x3 - p_x) == abs(y2 - p_y): 
        print(x3+dx1, y3+dy1)
    else:
        print(x3-dx1, y3-dy1)
elif abs(dx2) == abs(dy3) and abs(dy2) == abs(dx3):
    p_x = x2 + dx2
    p_y = y2 + dy2
    if abs(x1 - p_x) == abs(y2 - p_y) and abs(x2 - p_x) == abs(y1 - p_y): 
        print(x2+dx2, y2+dy2)
    else:
        print(x2-dx2, y2-dy2)
elif abs(dx1) == abs(dy3) and abs(dy1) == abs(dx3):
    p_x = x1 + dx3
    p_y = y1 + dy3
    if abs(x1 - p_x) == abs(y3 - p_y) and abs(x3 - p_x) == abs(y1 - p_y): 
        print(x1+dx3, y1+dy3)
    else:
        print(x1-dx3, y1-dy3)


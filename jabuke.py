def get_tri_area(x1, y1, x2, y2, x3, y3):
    x = [x1, x2, x3, x1]
    y = [y1, y2, y3, y1]
    se =0 
    sw = 0
    for i in range(3):
        se += x[i] * y[i+1]
    for i in range(3):
        sw += y[i] * x[i+1]
    return abs((se-sw)*(1/2)) 

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
n = int(input())

area = get_tri_area(x1,y1, x2,y2, x3,y3)
total = 0
for i in range(n):
    px, py = map(int, input().split())
    p1 = get_tri_area(px,py, x2,y2, x3,y3)
    p2 = get_tri_area(px,py, x1,y1, x3,y3)
    p3 = get_tri_area(px,py, x2,y2, x1,y1)
    if p1 + p2 + p3 <= area:
        total += 1
print('{:.1f}'.format(area))
print(total)



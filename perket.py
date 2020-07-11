import math


def helper(ing):
    p = tuple() 
    if len(ing) == 0:
        return p
    if len(ing) == 1:
        return ((ing[0],),)
    p += ((ing[0],),)
    for j in range(len(ing)-1):
        options = helper(ing[j+1:])
        for o in options:
            p += ((ing[0],) + o,)
    return p


def get_combs(ing):
    p = tuple() 
    for i in range(len(ing)):
        piece = helper(ing[i:])  
        p += piece 
    return p

n = int(input())
ing = [tuple(map(int, input().split())) for _ in range(n)]
diff = math.inf
perms = get_combs(ing)
for vals in perms:
    sour = 1
    bitter = 0
    for v in vals:
        s, b = v
        sour *= s
        bitter += b
    diff = min(diff, abs(sour - bitter))
print(diff)

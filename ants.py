# pretend each ant is wearing a hat, when 2 ants  collide, 
# they swap hats, so the answer of last ant to fall off 
# is the same as when the last hat falls off

# each individual hat never stops moving in the same direction
# so time in minimized by going to the closest edge
# time is maximized by going to the furthest edge

t = int(input())
for _ in range(t):
    l, n = map(int, input().split())
    ants = []
    while len(ants) < n:
        ants.extend(list(map(int, input().split())))

    min_t = 0 
    max_t = 0
    for a in ants:
        min_t = max(min_t, min(a, abs(l - a)))
        max_t = max(max_t, a, abs(l - a))
    print(min_t, max_t)


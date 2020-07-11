def saved(dmg, res):
    if dmg == 0 or res == 0:
        return 0

    l = (dmg & -dmg)
    s0, s1, s2, s3 = 0,0,0,0
    # either take left, right, or your own reserve
    if res & l:
        dmg = dmg & ~(l)
        res = res & ~(l)
        s0 = saved(dmg, res) + 1
        dmg = dmg | (l)
        res = res | (l)
    else:
        if res & (l << 1):
            dmg = dmg & ~(l)
            res = res & ~(l << 1)
            s1 = saved(dmg, res) + 1
            dmg = dmg | (l)
            res = res | (l << 1)
        if res & (l >> 1):
            dmg = dmg & ~(l)
            res = res & ~(l >> 1)
            s2 = saved(dmg, res) + 1
            dmg = dmg | (l)
            res = res | (l >> 1)
        
        # option where this kayak doesn't get saved at all
        dmg = dmg & ~(l)
        s3 = saved(dmg, res) 
        dmg = dmg | (l)
    return max(s0, s1, s2, s3)

n, s, r = map(int, input().split())
dmg = list(map(int, input().split()))
res = list(map(int, input().split()))
d_mask = 0
r_mask = 0
for i in dmg:
    d_mask = d_mask | (1<<(i-1))
for i in res:
    r_mask = r_mask | (1<<(i-1))

print(s - saved(d_mask, r_mask))




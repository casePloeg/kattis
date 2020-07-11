r,g,b,y,s = map(int, input().split())
memo = dict()

def prob(r, g, b, y, s):
    # ran out of fruits before crow finished s steps
    if r + g + b + y == 0 and s != 0:
        return 1
    elif s == 0:
        return 0
    # simulate rolling (generate states)
    if (r,g,b,y,s) in memo:
        return memo[(r,g,b,y,s)] 
    p = 0
    denom = 6
    # if there is no more of a certain fruit, prob of
    # rolling anything else is reduced
    vals = [r,g,b,y,s]
    m = 0 
    m_i = 0 
    for i, f in enumerate(vals):
        if i != 4 and f > m:
            m_i = i
            m = f
        if f == 0:
            denom -= 1
        else:
            vals[i] -= 1
            p += prob(*vals)
            vals[i] += 1
    # simulate rolling basket
    # there should always be a max that is greater than 
    # 0, and because theres equal prob for taking away
    # from any fruits, we just add the prob of taking one
    # of the maxes
    vals[m_i] -= 1
    p += prob(*vals)
    vals[m_i] += 1
    # equal chance for each action per roll, so we just
    # divide by the number of possible actions, 6 - the number
    # of fruit types that have 0 left
    p /= denom 

    memo[(r,g,b,y,s)] = p
    return p

# total number of configs is 5 * 5 * 5 * 5 * 9, fruit
# orientation doesn't really matter though so its really
# 5555 * 9 with proper optimizations
print(prob(r,g,b,y,s))

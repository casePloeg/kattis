from collections import defaultdict
t = int(input())
for _ in range(t):
    nat_freq = defaultdict(set)
    for_freq = defaultdict(set)

    n = int(input())
    pairs = set() 
    ing1_total = []
    ing2_total = []
    for i in range(n):
        pizza = input().strip()
        ing1 = input().split()
        ing1.pop(0)
        ing2 = input().split()
        ing2.pop(0)
        ing1_total.extend(ing1)
        ing2_total.extend(ing2)
        for w1 in ing1:
            nat_freq[w1].add(pizza)
        for w2 in ing2:
            for_freq[w2].add(pizza)
    ing1_total = set(ing1_total)
    ing2_total = set(ing2_total)
    for w1 in ing1_total:
        for w2 in ing2_total:
            if len(nat_freq[w1] ^ for_freq[w2]) == 0:
                pairs.add('(' + w1 + ', ' + w2 + ')')
    pairs = list(pairs)
    pairs.sort()
    print('\n'.join(pairs))
    print()
    

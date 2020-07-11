from collections import defaultdict


n = int(input())
courses = [sorted(list(map(int, input().split()))) for _ in range(n)]
pop = defaultdict(int)
most_pop = set()
pop_count = 0
for c in courses:
    pop[tuple(c)] += 1
    if pop[tuple(c)] > pop_count:
        pop_count = pop[tuple(c)]
        most_pop = {tuple(c)}
    elif pop[tuple(c)] == pop_count:
        most_pop.add(tuple(c))
print(len(most_pop) * pop_count)


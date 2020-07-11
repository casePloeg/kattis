n = int(input())

scores = []
for i in range(n):
    scores.append((int(input()), i))

cur_score = (1/5) * sum(map(lambda x: x[0] * (4/5)**x[1], scores))

avg = 0
for i in range(n):
    s = scores.copy()
    s.pop(i)
    avg += (1/5) * sum(map(lambda x: x[0] * (4/5)**(x[1] if x[1] <i else x[1]-1), s))
    
avg /= n

print(cur_score)
print(avg)


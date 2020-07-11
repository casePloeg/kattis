n = int(input())
p = 0
probs = sorted([float(input().split()[1]) for _ in range(n)], reverse=True)

for i in range(n):
    p += (i+1) * probs[i] 
print(p)


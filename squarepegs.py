n, m, k = map(int, input().split())
# radius
plots = [int(x) for x in input().split()]
circle_houses = [int(x) for x in input().split()]
sq_houses = [((int(x)**2)/2)**(1/2) for x in input().split()]
circle_houses += sq_houses
circle_houses.sort(reverse=True)
plots.sort(reverse=True)
i = 0
j = 0
total = 0
while i < (m + k) and j < n:
    if circle_houses[i] < plots[j]:
        total += 1
        j += 1
    i += 1
print(total)

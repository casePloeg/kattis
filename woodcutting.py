t = int(input())
for _ in range(t):
    n = int(input())
    avg = 0
    for i in range(n):
        wood = [int(x) for x in input().split()]
        avg += sum(wood[1:])/wood[0]
    avg /= n
    print(avg)

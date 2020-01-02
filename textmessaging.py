n = int(input())
for i in range(n):
    p, k, l = map(int, input().split())
    freq = [int(x) for x in input().split()]
    freq.sort(reverse=True)
    presses = 1
    total = 0
    index = 0
    while index < l:
        for j in range(k):
            if index == l:
                break
            total += freq[index] * presses
            index += 1
        presses += 1

    print('Case #' + str(i+1) + ':', total)

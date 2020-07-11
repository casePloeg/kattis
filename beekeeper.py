n = int(input())
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
while n != 0:
    fav = ""
    f_dub = -1
    for i in range(n):
        w = input().strip()
        double = 0
        j = 0
        while j < len(w)-1:
            if w[j] == w[j+1] and w[j] in vowels:
                double += 1
                j +=1
            j += 1
        if double > f_dub:
            f_dub = double
            fav = w
    print(fav)
    n = int(input())

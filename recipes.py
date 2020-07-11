t = int(input())
for i in range(t):
    r, p, d = map(int, input().split())
    ratio = d / p
    main = 0
    food = [input().split() for _ in range(r)]
    new_food = []
    for f in food:
        if float(f[2]) == 100:
            main = float(f[1]) * ratio
    for f in food:
        new_food.append(float(f[2])/100 * main)
    print('Recipe # ' + str(i+1))
    for j in range(r):
        print(food[j][0], new_food[j])
    print('-'*40)


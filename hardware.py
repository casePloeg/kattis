n = int(input())
for _ in range(n):
    street = input()
    building = input().split()
    b = int(building[0])
    orders = []
    while len(orders) < b:
        order = input().split()
        if order[0] == '+':
            s, t, interval = map(int, order[1:])
            for i in range(s, t+1, interval):
                orders.append(i)
        else:
            orders.append(int(order[0]))
    digits = [0 for i in range (10)]
    for order in orders:
        while order > 0:
            digits[order%10] += 1
            order = order // 10
    print(street)
    print(' '.join(building))
    for i, d in enumerate(digits):
        print('Make', str(d), 'digit', str(i))
    total = sum(digits)
    if total == 1:
        print('In total 1 digit')
    else:
        print('In total', str(total), 'digits')
                

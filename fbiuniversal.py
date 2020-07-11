def get_val(num, check):
    c = {'B': '8', 'G': 'C', 'I': '1', 'O': '0', 'Q': '0', 'S': '5', 'U': 'V', 'Y': 'V', 'Z': '2'}
    for i, n in enumerate(num):
        if n in c:
            num[i] = c[n]
    base = '0123456789ACDEFHJKLMNPRTVWX'
    multi = [2, 4, 5, 7, 8, 10, 11, 13]
    multi = multi[::-1]
    decimal = 0
    digit = 0
    for i, n in enumerate(num):
        decimal += (base.find(n)) * (27 ** i)
        digit += multi[i] * (base.find(n))
    digit %= 27
    if base[digit] == check:
        return decimal
    else:
        return 'Invalid'
    

p = int(input())
for _ in range(p):
    k, num = input().split()
    num = list(num)
    num, check = num[:-1][::-1], num[-1]

    print(k, get_val(num, check))

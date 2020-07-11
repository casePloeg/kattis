n = int(input())
a = sum([i for i in range(1, n+1)])
b = sum([i for i in range(2, n+2)])
even = (a % 2 == 0) or (b % 2 == 0)
odd = (a % 2 == 1) or (b % 2 == 1)
if even and odd:
    print('Either')
elif even:
    print('Even')
elif odd:
    print('Odd')


p = int(input())

for i in range(p):
    k, num = input().split()
    octal, decimal, hexa = 0,0,0
    valid = True
    num = num[::-1]
    for i, n in enumerate(num):
        n = int(n)
        if n < 8:
            octal += (n * (8 ** i))
        else:
            valid = False
        decimal += (n * (10 ** i))
        hexa += (n * (16 ** i))
    if not valid:
        octal = 0
    print(k, octal, decimal, hexa)
        

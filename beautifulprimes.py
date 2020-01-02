n = int(input())
for i in range(n):
    digits = int(input())
    num_elevens = digits
    num_sevens = 0
    while (11 ** num_elevens) * (7 ** num_sevens) > (10 ** (digits)) - 1:
        num_sevens += 1
        num_elevens -= 1
    primes = ['11' for i in range(num_elevens)] + ['7' for i in range(num_sevens)]
    print(' '.join(primes))

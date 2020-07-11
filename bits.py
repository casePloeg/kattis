def one_bits(n):
    c = 0
    # removes lowest one bit each iteration 
    while n:
        n &= n - 1
        c += 1

    return c 


t = int(input())
for _ in range(t):
    x = input().strip()
    bits = 0 
    for i in range(len(x)):
        bits = max(bits, one_bits(int(x[:i+1])))
    print(bits)

    

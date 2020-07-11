n, m = map(int, input().split())
while n + m != 0:
    carry = 0
    count = 0
    while n > 0 or m > 0:
        a, b = n % 10, m % 10
        a += carry
        # remember to "use up" the carry
        carry = 0
        if a + b > 9:
            carry = 1
            count += 1
        n //= 10
        m //= 10
    if count == 1:
        print(count, "carry operation.")
    elif count > 1:
        print(count, "carry operations.")
    else:
        print("No carry operation.")

    n, m = map(int, input().split())


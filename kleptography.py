n, m = map(int, input().split())

a = ['' for _ in range(m)]
back = input()
for i in range(n):
    a[-1-i] = back[-1-i]
b = input()
for i in reversed(range(n,m)):
    v_b = ord(b[i]) - ord("a")
    v_a = ord(a[i]) - ord("a")
    a[i-n] = chr((26 + v_b - v_a) % 26 + ord("a"))
print(''.join(a))

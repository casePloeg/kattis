c = input()
k = input()
msg = []
for i in range(len(c)):
    c_v = ord(c[i]) - ord("A")
    k_v = ord(k[i]) - ord("A")
    if i % 2 == 1:
        msg.append(chr(ord("A") + (c_v + k_v) % 26))
    else:
        msg.append(chr(ord("A") + (c_v - k_v + 26) % 26))
print(''.join(msg))


w = input()
size = len(w)
s1 = w[:size//3]
s2 = w[size//3:2*size//3]
s3 = w[2*size//3:]
if s1 == s2:
    print(s1)
elif s1 == s3:
    print(s1)
else:
    print(s2)


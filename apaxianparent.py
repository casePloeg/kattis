f, l = input().split()
if f[-2:] == 'ex':
	print(f + l)
elif f[-1] in {'a', 'i', 'o', 'u', 'e'}:
	print(f[:-1] + 'ex' + l)
else:
	print(f + 'ex' + l)


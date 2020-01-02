# https://open.kattis.com/problems/sortofsorting
num_names = int(input().strip())

while num_names != 0:
    names = []
    for i in range(num_names):
        names.append(input().strip())
    names.sort(key=lambda name: (name[:2]))
    print('\n'.join(names))
    print()

    num_names = int(input().strip())
n = int(input())
if (n == 1):
    print(0)
    exit()

carts = []
stack = []
for i in range(n):
    carts.append(int(input()))
days = 0
done = False
history = []
while not done:
    index = 0
    dir = 'asc'
    if carts[1] < carts[0]:
        dir = 'desc'
    while index < n - 1:
        if dir == 'asc' and carts[index + 1] < carts[index]:
            break
        elif dir == 'desc' and carts[index + 1] > carts[index]:
            break
        if (dir == 'asc' and carts[index + 1] - carts[index] > 1) or (dir == 'desc' and carts[index + 1] - carts[index] < -1):
            break
        index += 1
    if index == n - 1 and dir == 'asc':
        break
    else:
        history.append(index+1)
        carts = carts[index+1:] + carts[:index+1][::-1]

print(len(history))
print('\n'.join([str(x) for x in history]))
# print(carts)
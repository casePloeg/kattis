c, n = map(int, input().split())
on_train = 0
for i in range(n):
    left, entered, stay = map(int, input().split())
    on_train += entered
    on_train -= left
    if i == 0 and left > 0:
        print('impossible')
        exit()
    if i == n-1 and ((entered > 0 or stay > 0) or on_train > 0):
        print('impossible')
        exit()

    if on_train > c or on_train < 0 or (stay > 0 and on_train < c):
        print('impossible')
        exit()

print('possible')
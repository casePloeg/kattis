n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()
valid = False 
for i in range(n-2):
    a,b,c = sticks[i], sticks[i+1], sticks[i+2]
    # because input is sorted, checking the first
    # condition automatically satisfies the other two
    # picking a smaller a/b makes it harder, same for
    # picking a bigger c
    # so we can check linearly and get best results
    if a+b>c and a+c>b and b+c>a:
        valid = True
        print('possible')
        break
if not valid:
    print('impossible')


pairs = int(input())
stack1 = input().strip().split()
stack2 = []
moves = 0

while stack1:
    stack2.append(stack1.pop())
    moves += 1
    while stack1 and stack2 and stack1[-1] == stack2[-1]:
        stack1.pop()
        stack2.pop()
        moves += 1

if stack2:
    print('impossible')
else:
    print(moves)

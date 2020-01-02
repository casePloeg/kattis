num_cards = int(input())
stack1 = [int(i) for i in input().strip().split()]
stack2 = []

while stack1:
    stack2.append(stack1.pop())
    while stack1 and stack2 and (stack1[-1] + stack2[-1]) % 2 == 0:
        stack1.pop()
        stack2.pop()
print(len(stack2))
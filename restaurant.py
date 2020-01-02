# https://open.kattis.com/problems/restaurant

# stack2: has the current order to take from

# DROP 3
# DROP 5
# MOVE 2->1
# TAKE 8

# DROP 1 3
# DROP 2 5
# MOVE 1->2 3

# NEW DROP:
# MOVE 2->1 everything
# DROP 2 10
# MOVE 1->2 everything


# DROP:
# stack1: 
# stack2: 3, 5

# MOVE:
# stack1: 5, 3
# stack2: 

# TAKE:


# stack1: 40

# TAKE 50

# TAKE 1 40
# MOVE 2->1 everything
# TAKE 1 10

# Always take from 1
# when 1 is empty, flip everything in from 2
# always drop into 2


n = int(input())
while n != 0:
    stack1 = 0
    stack2 = 0
    for i in range(n):
        order, m = input().split()
        m = int(m)
        if order == 'DROP':
            print('DROP 2 ' + str(m))
            stack2 += m
        if order == 'TAKE':
            if stack1 < m:
                if stack1 > 0:
                    print('TAKE 1 ' + str(stack1))
                    m = m - stack1
                print('MOVE 2->1 ' + str(stack2))
                stack2, stack1 = 0, stack2
            print('TAKE 1 ' + str(m))
            stack1 -= m
    print()
    n = int(input())


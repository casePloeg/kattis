import math


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.s = 1

    def insert(self, val):
        self.s += 1
        if val < self.v:
            if self.l:
                self.l.insert(val)
            else:
                self.l = Node(val)
        else:
            if self.r:
                self.r.insert(val)
            else:
                self.r = Node(val)


def calculate(root):
    m = 0
    if root.l:
        m = root.l.s
    n = 0
    if root.r:
        n = root.r.s
    # take the total number of children of the root and
    # choose the amount of one of the subtrees, corresponds
    # to each possible sequence 
    res = math.factorial(m+n) // (math.factorial(n) * math.factorial(m))
    if root.l:
        res *= calculate(root.l)
    if root.r:
        res *= calculate(root.r)
    return int(res)


n = int(input())

while n != 0:
    seq = list(map(int, input().split()))
    root = Node(seq[0])
    for i in range(1, n):
        root.insert(seq[i])
    print(int(calculate(root)))
    n = int(input())

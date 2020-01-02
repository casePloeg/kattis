class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def insert_rec(root, val, depth):
#     if val < root.val:
#         if root.left == None:
#             root.left = BSTNode(val)
#             return depth + 1
#         else:
#             return insert_rec(root.left, val, depth + 1)
#     elif val > root.val:
#         if root.right == None:
#             root.right = BSTNode(val)
#             return depth + 1
#         else:
#             return insert(root.right, val, depth + 1)
#     else:
#         return depth


def insert(root, val):
    depth = 0
    cur = root
    prev = None
    while cur:
        if val < cur.val:
            prev = cur
            cur = cur.left
            depth += 1
            if not cur:
                prev.left = BSTNode(val)
        else:
            prev = cur
            cur = cur.right
            depth += 1
            if not cur:
                prev.right = BSTNode(val)
    return depth

c = 0
n = int(input())
root = None

for i in range(n):
    y = int(input())
    if not root:
        root = BSTNode(y)
        print(0)
        continue
    c += insert(root, y)
    print(c)
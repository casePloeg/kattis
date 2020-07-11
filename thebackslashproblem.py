import sys

def special(c):
    if ord('!') <= ord(c) <= ord('*'):
        return True
    elif ord('[') <= ord(c) <= ord(']'):
        return True
    else:
        return False


for line in sys.stdin:
    n = int(line)
    msg = list(input()) 
    for i in range(n): 
        new = []
        for c in msg:
            if special(c) :
                new.append("\\")
            new.append(c)
        msg = new
    print(''.join(msg))

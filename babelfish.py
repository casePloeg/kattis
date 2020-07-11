import sys


line = sys.stdin.readline().strip()
d = dict()
while len(line) != 0:
    eng, esl = line.split()
    d[esl] = eng
    line = sys.stdin.readline().strip()

for line in sys.stdin:
    line = line.strip()
    if line in d:
        print(d[line])
    else:
        print('eh')

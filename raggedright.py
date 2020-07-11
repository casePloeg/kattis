import sys


lengths = []
for line in sys.stdin:
    lengths.append(len(line))
m = max(lengths)
score = sum(map(lambda x: (m - x)**2, lengths[:-1]))
print(score)


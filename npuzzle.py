actual = [list(input()) for _ in range(4)]
desired = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', '.']]
total = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if actual[i][j] == desired[k][l] and (k,l) != (3,3):
                    total += abs(i-k) + abs(j - l)
print(total)

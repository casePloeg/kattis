import itertools

def solution(S):
    # write your code in Python 3.6
    count = 0
    cur = ''
    correct = ''
    for i in range(len(S)):
        if S[i] == cur and count >= 3:
            count += 1
        elif S[i] == cur and count < 3:
            count += 1
            correct += S[i]
        elif S[i] != cur:
            cur = S[i]
            correct += S[i]
            count = 1
    return correct

def has_repeating(string):
    chars = set()
    for c in string:
        if c not in chars:
            chars.add(c)
        else:
            return True
    return False

def get_concat_length(strings):
    total_length = 0
    string = ''
    for i in strings:
        string += i

    if has_repeating(string):
        return -1
    return len(string)

def solution2(A):
    length = 0
    saved = {}
    perms = []
    for i in range(len(A)):
        perms += list(itertools.combinations(A, i+1))
    for permutation in perms:
        length = max(length, get_concat_length(permutation))
    return length

def solution3(N, K):
    if N == 0:
        return ['']
    result = []
    for p in solution3(N - 1, K):
        for l in 'abc':
            if p[-1:] != l:
                result += [p + l]
    return result[:K]


print(solution3(3,15))

# print(solution2(['co','dil','ity']))
# print(solution('eedaaad'))
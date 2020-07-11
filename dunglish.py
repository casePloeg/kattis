from collections import defaultdict


n = int(input())
s = input().split()
m = int(input())
d_t_e = defaultdict(int)
d_t_e2 = dict() 
for i in range(m):
    d, e, c = input().split()
    d_t_e[(d, c)] += 1
    d_t_e2[(d,c)] = e

flag = True
translated = [] 
correct = True
for w in s:
    if d_t_e[(w, 'correct')] + d_t_e[(w, 'incorrect')] != 1:
        flag = False
        break
    else:
        if (w, 'correct') in d_t_e2:
            translated.append(d_t_e2[(w, 'correct')])
        else:
            correct = False
            translated.append(d_t_e2[(w, 'incorrect')])

if flag:
    print(' '.join(translated))
    if correct:
        print('correct')
    else:
        print('incorrect')

else:
    c = 1
    inc = 1
    for w in s:
        c *= d_t_e[(w, 'correct')]
        inc *= (d_t_e[(w, 'incorrect')] + d_t_e[(w, 'correct')])
    print(c, 'correct')
    print(inc-c, 'incorrect')



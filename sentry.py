def is_bad_word(word, bad_words):
    word = word.lower()
    res = False
    for bad_word in bad_words:
        glob_left, glob_right, b_word = bad_word
        if glob_left and glob_right:
            res = b_word in word
        elif glob_left:
            index = word.find(b_word)
            res = index > -1 and index + len(b_word) == len(word)
        elif glob_right:
            index = word.find(b_word)
            res = index == 0
        else:
            res = word == b_word
        if res:
            break
    return res

bad_words = input().split()
for idx, word in enumerate(bad_words):
    glob_left = (word[0] == '*')
    glob_right = (word[-1] == '*')
    if word.count('*') == len(word):
        bad_words.pop(idx)
    else:
        start = 1 if glob_left else 0
        end = -1 if glob_right else len(word)
        bad_words[idx] = (glob_left, glob_right, word[start:end])

og_message = input()
msg_len = len(og_message)
i = 0
msg_list = []
while i < msg_len:
    seq = ''
    while i < msg_len and og_message[i].isalnum():
        seq += og_message[i]
        i += 1
    if seq != '':
        msg_list.append(seq)
    seq = ''
    while i < msg_len and not og_message[i].isalnum():
        seq += og_message[i]
        i += 1
    if seq != '':
        msg_list.append(seq)

for idx, word in enumerate(msg_list):
    if word.isalnum() and is_bad_word(word, bad_words):
        msg_list[idx] = '*' * len(word)
print()
''.join([x for x in msg_list])
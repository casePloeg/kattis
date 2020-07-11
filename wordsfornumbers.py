import sys

nums = {0: 'zero', 1: 'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19: 'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60: 'sixty', 70: 'seventy', 80:'eighty', 90:'ninety'}

def to_text(w):
    res = []
    if w[0] == '1':
        return nums[int(w)]
    for i, c in enumerate(reversed(list(w))):
        if not(c == '0' and len(w) > 1):
            res.append(nums[int(c) * 10** i])
    return '-'.join(res[::-1])

for line in sys.stdin:
    words = line.split()
    for i, w in enumerate(words):
        if w.isnumeric():
            text = to_text(w)
            if i == 0:
                text = text[0].upper() + text[1:]
            words[i] = text 
    print(' '.join(words))

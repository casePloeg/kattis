n = int(input())
words = []
for i in range(n):
    words.append(input())
target = input()
count = 0
for w in words:
    ans = []
    for c in w:
        if c == ' ':
            ans.append('0')
        elif c >= "a" and c < "d":
            ans.append('2') 
        elif c >= "d" and c < "g":
            ans.append('3')
        elif c >= "g" and c < "j":
            ans.append('4') 
        elif c >= "j" and c < "m":
            ans.append('5') 
        elif c >= "m" and c < "p":
            ans.append('6') 
        elif c >= "p" and c < "t":
            ans.append('7') 
        elif c >= "t" and c < "w":
            ans.append('8') 
        elif c >= "w" and c <= "z":
            ans.append('9') 
    if ''.join(ans) == target:
        count += 1
print(count)

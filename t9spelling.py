n = int(input())
for i in range(n):
    msg = input()
    ans = []
    for c in msg:
        if c == ' ':
            ans.append('0')
        elif c >= "a" and c < "d":
            ans.append('2' * ((ord(c) - ord('a'))%3 + 1)) 
        elif c >= "d" and c < "g":
            ans.append('3' * ((ord(c) - ord('d'))%3 + 1)) 
        elif c >= "g" and c < "j":
            ans.append('4' * ((ord(c) - ord('g'))%3 + 1)) 
        elif c >= "j" and c < "m":
            ans.append('5' * ((ord(c) - ord('j'))%3 + 1)) 
        elif c >= "m" and c < "p":
            ans.append('6' * ((ord(c) - ord('m'))%3 + 1)) 
        elif c >= "p" and c < "t":
            ans.append('7' * ((ord(c) - ord('p'))%4 + 1)) 
        elif c >= "t" and c < "w":
            ans.append('8' * ((ord(c) - ord('t'))%3 + 1)) 
        elif c >= "w" and c <= "z":
            ans.append('9' * ((ord(c) - ord('w'))%4 + 1)) 
    res = ''
    prev = ''
    for a in ans:
        if prev.startswith(a[0]):
            res += ' ' + a
        else:
            res += a
        prev = a
    print("Case #" + str(i+1) + ": " + res)


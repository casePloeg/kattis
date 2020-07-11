s = input().split(':')
t = input().split(':')

sec = int(t[-1]) - int(s[-1])
borrow = 0
if sec < 0:
    borrow = 1
    sec += 60
min_ = int(t[-2]) - int(s[-2])
if borrow:
    min_ -= 1

if min_ < 0:
    borrow = 1
    min_ += 60
else:
    borrow = 0

hour = int(t[-3]) - int(s[-3])
if borrow:
    hour -= 1

if hour < 0:
    hour += 24
res = [hour, min_, sec]
if res == [0, 0, 0]:
    res[0] = 24
print(':'.join(['{:02d}'.format(i) for i in res]))




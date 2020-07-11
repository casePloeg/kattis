n, d = map(int,input().split())
prev_yrs = list(map(int, input().split()))
found = False
for i, di in enumerate(prev_yrs):
    if d >= di:
        found = True
        print("It hadn't snowed this early in " + str(i) + " years!")
        break
if not found:
    print("It had never snowed this early!")


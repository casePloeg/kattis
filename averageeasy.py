t = int(input())
for _ in range(t):
    input()
    cs, e = map(int, input().split())
    cs_students = list(map(int, input().split()))
    e_students = list(map(int, input().split()))
    cs_sum = sum(cs_students) 
    e_sum = sum(e_students) 
    cs_average = cs_sum / cs
    e_average = e_sum / e
    count =0 
    for s in cs_students:
        new_cs = ((cs_sum - s) / (cs - 1))
        new_e  = ((e_sum + s) / (e + 1))
        if new_cs > cs_average and new_e > e_average:
            count += 1
    print(count)
    


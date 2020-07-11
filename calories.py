gram_t_cal = dict()
gram_t_cal[0] = 4
gram_t_cal[1] = 4
gram_t_cal[2] = 4
gram_t_cal[3] = 7
gram_t_cal[4] = 9

while True:
    items = []
    food = input()
    while food != '-':
        items.append(food.split())
        food = input()
    if len(items) == 0:
        break
    else:
        total_fat = 0
        total_cal = 0
        for item in items:
            fat, pro, sug, sta, alc = item
            sub_total = 0
            sub_percent = 0 
            for i, v in enumerate([pro, sug, sta, alc, fat]):
                if v[-1] == 'C':
                    sub_total += int(v[:-1])
                elif v[-1] == 'g':
                    sub_total += int(v[:-1]) * gram_t_cal[i] 
                elif v[-1] == '%':
                    sub_percent += int(v[:-1])
                    
            sub_total += (sub_total / (100 - sub_percent) * sub_percent)
            total_cal += sub_total
            if fat[-1] == 'C':
                total_fat += int(fat[:-1])
            elif fat[-1] == 'g':
                total_fat += int(fat[:-1]) * 9
            else:
                total_fat += sub_total / 100 * int(fat[:-1]) 
        print(round(total_fat/total_cal*100), '%', sep='')

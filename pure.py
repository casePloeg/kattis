def compute_number_score(number):
    score = 0
    if number % 3 == 0:
        score += 4
    seq = 0
    twos = 0
    last = -2
    while number > 0:
        digit = number % 10


        if (last != digit - 1):
            score += seq * seq
            seq = 1
        else:
            seq += 1

        if digit == 7:
            score += 5

        if digit == 2:
            twos += 1
        else:
            twos = 0

        if twos > 1:
            score += 6

        if digit % 2 == 0:
            score += 3
        last = digit
        number = number // 10
    score += seq * seq
    return score

print(compute_number_score(321222158))
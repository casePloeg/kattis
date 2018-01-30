import sys


# get the info for the question as a list
info = sys.stdin.readline().split()
num_info = []
# convert elements to integers in a new list
for i in range(0, len(info)):
    num_info.append(int(info[i]))
# create list for possible operations
operations = [('+', '='), ('=', '+'),
              ('-', '='), ('=', '-'),
              ('*', '='), ('=', '*'),
              ('/', '='), ('=', '/')]
              
# create variable to keep track of whether a valid operation was found or not
is_valid_operation = False
# create a counter for the operations
oper = 0

while(not is_valid_operation):
    equal_first = False
    plus_first = False
    minus_first = False
    multi_first = False
    div_first = False
    plus_sec = False
    minus_sec = False
    multi_sec = False
    div_sec = False
    # create a list for the current operations
    cur_op = operations[oper]
    # determine whether the operation is valid or not
    if(cur_op[0] == '='):
        equal_first = True
    elif(cur_op[0] == '+'):
        plus_first = True
    elif(cur_op[0] == '-'):
        minus_first = True
    elif(cur_op[0] == '*'):
        multi_first = True
    elif(cur_op[0] == '/'):
        div_first = True

    if(equal_first):
        if(cur_op[1] == '+'):
            plus_sec = True
        elif(cur_op[1] == '-'):
            minus_sec = True
        elif(cur_op[1] == '*'):
            multi_sec = True
        elif(cur_op[1] == '/'):
            div_sec = True        

    if(equal_first):
        if(plus_sec):
            if(num_info[0] == num_info[1] + num_info[2]):
                is_valid_operation = True
                print(info[0] + '=' + info[1] + '+' + info[2])
        elif(minus_sec):
            if(num_info[0] == num_info[1] - num_info[2]):
                is_valid_operation = True
                print(info[0] + '=' + info[1] + '-' + info[2])
        elif(multi_sec):
            if(num_info[0] == num_info[1] * num_info[2]):
                is_valid_operation = True
                print(info[0] + '=' + info[1] + '*' + info[2])
        elif(div_sec):
            if(num_info[0] == num_info[1] / num_info[2]):
                is_valid_operation = True
                print(info[0] + '=' + info[1] + '/' + info[2])
    else:
        if(plus_first):
            if(num_info[0] + num_info[1] == num_info[2]):
                is_valid_operation = True
                print(info[0] + '+' + info[1] + '=' + info[2])
        elif(minus_first):
            if(num_info[0] - num_info[1] == num_info[2]):
                is_valid_operation = True
                print(info[0] + '-' + info[1] + '=' + info[2])
        elif(multi_first):
            if(num_info[0] * num_info[1] == num_info[2]):
                is_valid_operation = True
                print(info[0] + '*' + info[1] + '=' + info[2])
        elif(div_first):
            if(num_info[0] / num_info[1] == num_info[2]):
                is_valid_operation = True
                print(info[0] + '/' + info[1] + '=' + info[2])
    oper += 1
import sys


# get the number of questions
n = int(sys.stdin.readline())
# create a counter for Adrian's correct answers
adrian = 0
# Bruno's
bruno = 0
# Goran's
goran = 0
# get the string of correct answers
answers = sys.stdin.readline().replace('\n','')
# iterate through the answers
for i in range(0,n):
    # calculate the number of answers the boys got right
    if(i % 12 == 0):
        if(answers[i] == 'A'):
            adrian += 1
        elif(answers[i] == 'B'):
            bruno += 1
        elif(answers[i] == 'C'):
            goran += 1
    elif(i % 12 == 1):
        if(answers[i] == 'A'):
            bruno += 1
        elif(answers[i] == 'B'):
            adrian += 1
        elif(answers[i] == 'C'):
            goran += 1
    elif(i % 12 == 2):
        if(answers[i] == 'A'):
            goran += 1
        elif(answers[i] == 'B'):
            bruno += 1
        elif(answers[i] == 'C'):
            adrian += 1
    elif(i % 12 == 3):
        if(answers[i] == 'A'):
            adrian += 1
            goran += 1
        elif(answers[i] == 'C'):
            bruno += 1
    elif(i % 12 == 4):
        if(answers[i] == 'B'):
            goran += 1
            bruno += 1
            adrian += 1
    elif(i % 12 == 5):
        if(answers[i] == 'A'):
            bruno += 1
        elif(answers[i] == 'B'):
            goran += 1  
        elif(answers[i] == 'C'):
            adrian += 1
    elif(i % 12 == 6):
        if(answers[i] == 'A'):
            adrian += 1
        elif(answers[i] == 'B'):
            bruno += 1
        elif(answers[i] == 'C'):
            goran += 1
    elif(i % 12 == 7):
        if(answers[i] == 'A'):
            pass
        elif(answers[i] == 'B'):
            adrian += 1
        elif(answers[i] == 'C'):
            goran += 1
            bruno += 1
    elif(i % 12 == 8):
        if(answers[i] == 'A'):
            goran += 1
        elif(answers[i] == 'B'):
            bruno += 1
        elif(answers[i] == 'C'):
            adrian += 1
    elif(i % 12 == 9):
        if(answers[i] == 'A'):
            adrian += 1
            goran += 1
            bruno += 1 
    elif(i % 12 == 10):
        if(answers[i] == 'B'):
            adrian += 1
            goran += 1
            bruno += 1
    elif(i % 12 == 11):
        if(answers[i] == 'B'):
            goran += 1
        elif(answers[i] == 'C'):
            adrian += 1
            bruno += 1

correct_list = [adrian, bruno, goran]
correct_list.sort()
print(correct_list[-1])
if(adrian == correct_list[-1]):
    print('Adrian')
if(bruno == correct_list[-1]):
    print('Bruno')
if(goran == correct_list[-1]):
    print('Goran')
import sys


# get the drm message
msg = sys.stdin.readline().replace('\n','')
# create a variable for the length of the message
msg_len = len(msg)
# create a variable for half the length
h_len = msg_len // 2
# split the message in half
half1 = msg[:h_len]
half2 = msg[h_len:]
# create a dict that maps values 0 - 25 to letters A - Z
value_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
                   7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
                   14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
                   20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
# create a dictionary that maps letter to value
letter_to_value = {}
for key in value_to_letter:
    letter_to_value[value_to_letter[key]] = key
# calculate rotate value for each half
rotate1 = 0
rotate2 = 0
for char in half1:
    rotate1 += letter_to_value[char]
for char in half2:
    rotate2 += letter_to_value[char]
# create variables for the converted half
converted = ''
# iterate through the halves
for i in range(0, len(half1)):
    # get current letters value
    letter_val = ((letter_to_value[half1[i]] + rotate1) % 26)
    letter2_val = ((letter_to_value[half2[i]] + rotate2) % 26)
    letter_val = (letter_val + letter2_val) % 26
    converted = converted + value_to_letter[letter_val]
# output the converted half
print(converted)
import sys


# get the sentence that needs to be translated (read as lower case)
sent = sys.stdin.readline().replace('\n','').lower()

# create dictionary for characters of new alpha
old_to_new = {'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '#',
              'g': '6', 'h': '[-]', 'i': '|', 'j': '_|', 'k': '|<', 'l': '1',
              'm': '[]\/[]', 'n': '[]\[]', 'o': '0', 'p': '|D', 'q': '(,)',
              'r': '|Z', 's': '$', 't': "']['", 'u': '|_|', 'v': '\/',
              'w': '\/\/', 'x': '}{', 'y': '`/', 'z': '2'}
# create variable for translated message
msg = ''
# iterate through the given sentence
for char in sent:
    # if the char is in the dictionary then it is converted and then added to
    # the message
    if(char in old_to_new):
        msg = msg + old_to_new[char]
    # otherwise add the current char to the message
    else:
        msg = msg + char
# output the translated sentence
print(msg)
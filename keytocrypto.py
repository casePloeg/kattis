import sys


# get the encrypted message
en_msg = sys.stdin.readline().replace('\n','').lower()
# get the secret word
word = sys.stdin.readline().replace('\n','').lower()

# create a variable for the decrypted message
msg = ''
# create a variable for the key. The key will start with the given
# secret word
key = word
# iterate through the encrypted message
for i in range(0, len(en_msg)):
    # the letter that corresponds to the current encrypted letter is the
    # encrypted letter shift backwards by the value of the corresponding key
    # letter
    decyrpt_letter = chr((((ord(en_msg[i]) - 97) - (ord(key[i]) - 97)) % 26) + 97)
    # append the decrypted letter to the decrypted message as well as the key
    key = key + decyrpt_letter
    msg = msg + decyrpt_letter.upper()
# output the decrypted message
print(msg)
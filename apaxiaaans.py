import sys


# get the word
word = sys.stdin.readline().replace('\n','')

# create a variable for the word that will have consectutive letters removed
filtered_word = ''
# iterate through the word
counter = 0
while(counter < len(word)):
    # add the letter to the filtered_word
    filtered_word = filtered_word + word[counter]
    # create a variable to keep track of unique letters
    unique = False
    # if the next letter is the same skip over it until a new letter is found
    # or the end of the word is reached
    counter += 1
    while((not unique) and (counter < len(word))):
        # if the next letter is unique end the loop
        if(word[counter] != word[counter - 1]):
            unique = True
        # else, increment the counter by 1
        else:
            counter += 1

# output the filtered word 
print(filtered_word)
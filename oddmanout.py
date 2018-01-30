import sys


# get the number of test cases
n = int(sys.stdin.readline())
# iterate through the test cases
for i in range(0, n):
    # get the number of guests
    g = int(sys.stdin.readline())
    # get the guest numbers as a list
    gst_num = sys.stdin.readline().split()
    # create a set for guest numbers
    gst_num_set = set()
    # iterate through the numbers
    for num in gst_num:
        # if the number is in the set already, take it out of the set
        if(num in gst_num_set):
            gst_num_set.discard(num)
        # if the number is not in the set already add it to the set
        else:
            gst_num_set.add(num)
    # there should only be 1 number left
    # output the number that is left
    msg = 'Case #' + str(i + 1) + ': ' + str(gst_num_set.pop())
    print(msg)

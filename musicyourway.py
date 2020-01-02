# https://open.kattis.com/problems/musicyourway
# read attribute types and song info
attributes = input().strip().split()
num_songs = int(input().strip())

# yoink that song info into a 2d array
songs = []
for i in range(num_songs):
    songs.append(input().strip().split())

# figure out how to sort it
num_sorts = int(input().strip())
for i in range(num_sorts):
    # do the sort
    attribute = input()
    index = attributes.index(attribute)
    songs.sort(key=lambda a: (a[index]))

    # print the post-sort result
    print(' '.join(attributes))
    print('\n'.join([' '.join(song) for song in songs]))
    if i < num_sorts - 1:
        print()




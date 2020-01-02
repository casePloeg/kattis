num_members, num_songs = map(int, input().split())
grid = []
for i in range(num_members):
    line = [int(_) for _ in input().strip().split()]
    grid.append(line)

unfilled = 0
songs = 0
col_index = 0
wanted_songs = [0 for i in range(num_songs)]
while unfilled > 0 or songs == 0 and col_index < num_songs:
    # get the songs
    column = []
    for i in range(num_members):
        column.append(grid[i][col_index])
    # loop through songs
    for song_num in column:
        if wanted_songs[song_num - 1] == 0:
            unfilled += 1
            songs += 1
        if wanted_songs[song_num - 1] >= num_members - 1:
            unfilled -= 1
        wanted_songs[song_num - 1] += 1
    col_index += 1

print(songs)
set_list = ''
for i in range(num_songs):
    if wanted_songs[i] == num_members:
        set_list += str(i + 1) + ' '
print(set_list.strip())

def output_result(result_grid, num_rings):
    # square size based on output requirements
    if num_rings < 10:
        square_size = 2
    else:
        square_size = 3

    # output the grid with the appropriate square size
    for i in range(len(result_grid)):
        output_line = ""
        for j in range(len(result_grid[i])):
            ring_num = str(result_grid[i][j])
            if ring_num == "0":
                ring_num = "."
            # if only one dot is required (remaining space in square taken by ring number)
            if square_size == 2 or len(ring_num) > 1:
                output_line += "." + ring_num
            # if two dots are required (3 character square with 1 digit ring number)
            else:
                output_line += ".." + ring_num
        print(output_line)

def set_value(result_grid, i, j, ring_num):
    rows = len(result_grid)
    cols = len(result_grid[0])
    neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
    for neighbour in neighbours:
        n_row, n_col = neighbour
        # if neighbour is out of bounds , set to num
        neighbour_out_of_bounds = not (0 <= n_row < rows and 0 <= n_col < cols)
        # if neighbour is num - 1, set to num
        neighbour_less_ring = not neighbour_out_of_bounds and result_grid[
            n_row][n_col] == ring_num - 1
        if neighbour_out_of_bounds or neighbour_less_ring:
            result_grid[i][j] = ring_num
            return True
    return False


# read in the original tree grid given number of rows and columns
rows, cols = map(int, input().strip().split())
tree_grid = []

for i in range(rows):
    tree_grid.append(input().strip())
# initialize result grid to 0 in place of dots, -1 in place of t (to be given ring value)
result_grid = [[0 if tree_grid[i][j] == "." else -1 for j in range(cols)] for i in range(rows)]

set_new_ring_num = True # if a position was assigned a new ring number
ring_num = 0
while set_new_ring_num:
    ring_num += 1
    set_new_ring_num = False
    for i in range(rows):
        for j in range(cols):
            if result_grid[i][j] == -1:
                set_new_ring_num = set_value(result_grid, i, j, ring_num) or set_new_ring_num

output_result(result_grid, ring_num - 1)

n = int(input())
m = int(input())
elevations = [[] for i in range(n)]
for i in range(n):
    elevations[i] = input().split()

n = len(elevations)
m = len(elevations[0])
high_set = set()
high_points = [[0 for j in range(len(elevations[0]))] for i in range(len(elevations))]
for i in range(len(elevations)):
    for j in range(len(elevations[0])):
        is_high = True
        # check top
        if i > 0:
            if elevations[i][j] < elevations[i-1][j]:
                is_high = False
        # left
        if j > 0:
            if elevations[i][j] < elevations[i][j-1]:
                is_high = False
        # bottom
        if i < n - 1:
            if elevations[i][j] < elevations[i+1][j]:
                is_high = False
        # right
        if j < m - 1:
            if elevations[i][j] < elevations[i][j+1]:
                is_high = False
        if i > 0 and j > 0:
            if elevations[i][j] < elevations[i-1][j-1]:
                is_high = False
        if i > 0 and j < m - 1:
            if elevations[i][j] < elevations[i-1][j+1]:
                is_high = False
        if i < n - 1 and j > 0:
            if elevations[i][j] < elevations[i+1][j-1]:
                is_high = False
        if i < n - 1 and j < m - 1:
            if elevations[i][j] < elevations[i+1][j+1]:
                is_high = False
        if is_high:
            high_points[i][j] = 1
            high_set.add((i, j))



def flood(i, j, high_points, elevations, visited):
    #top
    if i > 0:
        if elevations[i][j] > elevations[i - 1][j] and not visited[i - 1][j]:
            high_points[i - 1][j] += 1
            visited[i - 1][j] = True
            flood(i-1, j, high_points, elevations, visited)
    # left
    if j > 0:
        if elevations[i][j] > elevations[i][j - 1] and not visited[i][j - 1]:
            high_points[i][j - 1] += 1
            visited[i][j - 1] = True
            flood(i, j - 1, high_points, elevations, visited)
    # bottom
    if i < n - 1:
        if elevations[i][j] > elevations[i + 1][j] and not visited[i + 1][j]:
            high_points[i + 1][j] += 1
            visited[i + 1][j] = True
            flood(i + 1, j, high_points, elevations, visited)
    # right
    if j < m - 1:
        if elevations[i][j] > elevations[i][j + 1] and not visited[i][j + 1]:
            high_points[i][j + 1] += 1
            visited[i][j + 1] = True
            flood(i, j + 1, high_points, elevations, visited)
    if i > 0 and j > 0:
        if elevations[i][j] > elevations[i - 1][j - 1] and not visited[i - 1][j - 1]:
            high_points[i - 1][j - 1] += 1
            visited[i - 1][j - 1] = True
            flood(i - 1, j - 1, high_points, elevations, visited)
    if i > 0 and j < m - 1:
        if elevations[i][j] > elevations[i - 1][j + 1] and not visited[i - 1][j + 1]:
            high_points[i - 1][j + 1] += 1
            visited[i - 1][j + 1] = True
            flood(i - 1, j + 1, high_points, elevations, visited)
    if i < n - 1 and j > 0:
        if elevations[i][j] > elevations[i + 1][j - 1] and not visited[i + 1][j - 1]:
            high_points[i + 1][j - 1] += 1
            visited[i + 1][j - 1] = True
            flood(i + 1, j - 1, high_points, elevations, visited)
    if i < n - 1 and j < m - 1:
        if elevations[i][j] > elevations[i + 1][j + 1] and not visited[i + 1][j + 1]:
            high_points[i + 1][j + 1] += 1
            visited[i + 1][j + 1] = True
            flood(i + 1, j + 1, high_points, elevations, visited)

    return high_points


# to find plateaus, flood when equal and set points to 1 instead of increasing
def flood2(i, j, high_points, elevations, visited):
    #top
    if i > 0:
        if elevations[i][j] == elevations[i - 1][j] and not visited[i - 1][j] and high_points[i - 1][j] == 0:
            high_points[i][j] = 0
            visited[i - 1][j] = True
        elif elevations[i][j] == elevations[i - 1][j] and not visited[i - 1][j]:
            visited[i - 1][j] = True
            flood2(i-1, j, high_points, elevations, visited)
    # left
    if j > 0:
        if elevations[i][j] == elevations[i][j - 1] and not visited[i][j - 1] and high_points[i][j - 1] == 0:
            high_points[i][j] = 0
            visited[i][j - 1] = True
        elif elevations[i][j] == elevations[i][j - 1] and not visited[i][j - 1]:
            visited[i - 1][j] = True
            flood2(i, j - 1, high_points, elevations, visited)
    # bottom
    if i < n - 1:
        if elevations[i][j] == elevations[i + 1][j] and not visited[i + 1][j] and high_points[i + 1][j] == 0:
            high_points[i][j] = 0
            visited[i + 1][j] = True
        elif elevations[i][j] == elevations[i + 1][j] and not visited[i + 1][j]:
            visited[i + 1][j] = True
            flood2(i + 1, j, high_points, elevations, visited)
    # right
    if j < m - 1:
        if elevations[i][j] == elevations[i][j + 1] and not visited[i][j + 1] and high_points[i][j + 1] == 0:
            high_points[i][j] = 0
            visited[i][j + 1] = True
        elif elevations[i][j] == elevations[i][j + 1] and not visited[i][j + 1]:
            visited[i][j + 1] = True
            flood2(i, j + 1, high_points, elevations, visited)
    if i > 0 and j > 0:
        if elevations[i][j] == elevations[i - 1][j - 1] and not visited[i - 1][j - 1] and high_points[i - 1][j - 1] == 0:
            high_points[i][j] = 0
            visited[i - 1][j - 1] = True
        elif elevations[i][j] == elevations[i - 1][j - 1] and not visited[i - 1][j - 1]:
            visited[i - 1][j - 1] = True
            flood2(i - 1, j - 1, high_points, elevations, visited)
    if i > 0 and j < m - 1:
        if elevations[i][j] == elevations[i - 1][j + 1] and not visited[i - 1][j + 1] and high_points[i - 1][j + 1] == 0:
            high_points[i][j] = 0
            visited[i - 1][j + 1] = True
        elif elevations[i][j] == elevations[i - 1][j + 1] and not visited[i - 1][j + 1]:
            visited[i - 1][j + 1] = True
            flood2(i - 1, j + 1, high_points, elevations, visited)
    if i < n - 1 and j > 0:
        if elevations[i][j] == elevations[i + 1][j - 1] and not visited[i + 1][j - 1] and high_points[i + 1][j - 1] == 0:
            high_points[i][j] = 0
            visited[i + 1][j - 1] = True
        elif elevations[i][j] == elevations[i + 1][j - 1] and not visited[i + 1][j - 1]:
            flood2(i + 1, j - 1, high_points, elevations, visited)
            visited[i + 1][j - 1] = True
    if i < n - 1 and j < m - 1:
        if elevations[i][j] == elevations[i + 1][j + 1] and not visited[i + 1][j + 1] and high_points[i + 1][j + 1] == 0:
            high_points[i][j] = 0
            visited[i + 1][j + 1] = True
        elif elevations[i][j] == elevations[i + 1][j + 1] and not visited[i + 1][j + 1]:
            flood2(i + 1, j + 1, high_points, elevations, visited)
            visited[i + 1][j + 1] = True

    return high_points

# take high points and do flood analysis
while len(high_set) > 0:
    (i, j) = high_set.pop()
    visited = [[False for j in range(m)] for i in range(n)]
    flood2(i, j, high_points, elevations, visited)


print(high_points)
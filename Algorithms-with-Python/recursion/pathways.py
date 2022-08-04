def find_possible_paths(row, col, pathways, direction, path, result):

    if row < 0 or col < 0 or row >= len(pathways) or col >= len(pathways[0]):  # set dimensions limits
        return

    if pathways[row][col] == 'v':  # checks if position is being used
        return

    path.append(direction)  # keeps current route state

    if pathways[row][col] == 'e':
        result.append(''.join(path))
        print(f"{len(result)}. - {''.join(path)}")

    else:
        pathways[row][col] = 'v'  # paves the already taken routes
        find_possible_paths(row + 1, col, pathways, 'D', path, result)
        find_possible_paths(row, col + 1, pathways, 'R', path, result)
        pathways[row][col] = '-'  # when calls finished, take path back to its original state

    path.pop()  # clear current route state

rows = int(input())
cols = int(input())

pathways = []
for i in range(rows):
    lst = []
    for j in range(cols):
        lst.append('-')
    pathways.append(lst)

pathways[rows - 1][cols - 1] = 'e'
find_possible_paths(0, 0, pathways, '', [], [])  # initiate starting point and the matrix
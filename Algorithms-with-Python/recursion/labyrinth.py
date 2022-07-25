def find_possible_paths(row, col, labyrinth, direction, path):

    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[0]):  # set dimensions limits
        return

    if labyrinth[row][col] == '*':  # a 'stop' sign
        return

    if labyrinth[row][col] == 'v':  # checks if position is being used
        return

    path.append(direction)  # keeps current route state

    if labyrinth[row][col] == 'e':
        print(''.join(path))
    else:
        labyrinth[row][col] = 'v'  # # paves the already taken routes
        find_possible_paths(row - 1, col, labyrinth, 'U', path)
        find_possible_paths(row + 1, col, labyrinth, 'D', path)
        find_possible_paths(row, col - 1, labyrinth, 'L', path)
        find_possible_paths(row, col + 1, labyrinth, 'R', path)
        labyrinth[row][col] = '-'  # when calls finished, take path back to its original state

    path.pop()  # clear current route state


rows = int(input())
col = int(input())

labyrinth = []
for _ in range(rows):
    labyrinth.append(list(input()))

find_possible_paths(0, 0, labyrinth, '', [])  # initiate starting point and the labyrinth

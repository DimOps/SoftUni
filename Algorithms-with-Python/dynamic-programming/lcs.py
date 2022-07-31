from collections import deque

first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

lcs = []

[lcs.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            lcs[row][col] = lcs[row - 1][col - 1] + 1
        else:
            lcs[row][col] = max(lcs[row - 1][col], lcs[row][col - 1])
print(f'Length of squence: {lcs[rows - 1][cols - 1]}')

row = rows - 1
col = cols - 1
lcs_sequence = deque()

while row > 0 and col > 0:
    if first[row - 1] == second[col - 1]:
        lcs_sequence.appendleft(first[row - 1])
        row -= 1
        col -= 1
    elif lcs[row - 1][col] > lcs[row][col - 1]:
        row -= 1
    else:
        col -= 1

print(*lcs_sequence, sep='')

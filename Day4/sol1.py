import os
dir = os.getcwd()

with open("input.txt", "r") as my_file:
    data = my_file.read()

grid = [list(string) for string in data.split('\n')]
gridR = [row.copy() for row in grid]
# transpose then flip the matrix -> get rotated matrix 90 deg right
for i in range(len(gridR)):
    for j in range(i + 1):
        gridR[i][j], gridR[j][i] = gridR[j][i], gridR[i][j]
for i in range(len(gridR)):
    gridR[i].reverse()


res = 0
# check for rows
for row in grid:
    for i in range(len(grid[0]) - 3):
        if ''.join(row[i:i + 4]) == 'XMAS':
            res += 1
        elif ''.join(row[i:i + 4]) == 'SAMX':
            res += 1
# check for columns
for row in gridR:
    for i in range(len(gridR[0]) - 3):
        if ''.join(row[i:i + 4]) == 'XMAS':
            res += 1
        elif ''.join(row[i:i + 4]) == 'SAMX':
            res += 1
# check right diagonal
for i in range(len(grid)):
    for j in range(len(grid[0])):
        word = ""
        for diff in range(4):
            if i + diff < len(grid) and j + diff < len(grid[0]):
                word += grid[i + diff][j + diff]
        if word == 'XMAS':
            res += 1
        elif word == 'SAMX':
            res += 1
# check left diagonal
for i in range(len(gridR)):
    for j in range(len(gridR[0])):
        word = ""
        for diff in range(4):
            if i + diff < len(gridR) and j + diff < len(gridR[0]):
                word += gridR[i + diff][j + diff]
        if word == 'XMAS':
            res += 1
        elif word == 'SAMX':
            res += 1
print(res)

my_file.close()
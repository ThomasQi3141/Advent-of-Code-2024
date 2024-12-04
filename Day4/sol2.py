import os
dir = os.getcwd()

with open("input.txt", "r") as my_file:
    data = my_file.read()

grid = data.split('\n')

res = 0

# check all X's
for i in range(len(grid)):
    for j in range(len(grid[0])):
        word1 = ""
        word2 = ""
        for diff in range(3):
            if 0 <= i + diff < len(grid) and 0 <= j + diff < len(grid[0]):
                word1 += grid[i + diff][j + diff]
            if 0 <= i + diff < len(grid) and 0 <= j + 2 - diff < len(grid[0]):
                word2 += grid[i + diff][j + 2 - diff]
        if (word1 == 'MAS' or word1 == 'SAM') and (word2 == 'MAS' or word2 == 'SAM'):
            res += 1
print(res)

my_file.close()
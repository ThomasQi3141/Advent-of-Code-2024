import os
dir = os.getcwd()

with open("input.txt", "r") as my_file:
    data = my_file.read()

splitData = data.split("mul(")

res = 0
for i, s in enumerate(splitData):
    idx = s.find(')')
    if idx < 0:
        continue
    middle = s[:idx]
    splitMid = middle.split(',')
    if len(splitMid) != 2 or not splitMid[0].isdigit() or not splitMid[1].isdigit():
        continue
    res += int(splitMid[0]) * int(splitMid[1])
print(res)

my_file.close()
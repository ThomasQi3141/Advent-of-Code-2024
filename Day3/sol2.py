import os
dir = os.getcwd()

with open("input.txt", "r") as my_file:
    data = my_file.read()

data = 'do()' + data

def doMult(string):
    res = 0
    splitData = string.split("mul(")
    for i, s in enumerate(splitData):
        idx = s.find(')')
        if idx < 0:
            continue
        middle = s[:idx]
        splitMid = middle.split(',')
        if len(splitMid) != 2 or not splitMid[0].isdigit() or not splitMid[1].isdigit():
            continue
        res += int(splitMid[0]) * int(splitMid[1])
    return res

res = 0

def findIndices(string, sub):
    res = []
    start = 0
    while True:
        start = string.find(sub, start)
        if start == -1:
            break
        res.append(start)
        start += 1
    return res
# find all pairs of don't() -> do()
dontIdx = findIndices(data, "don't()")
doIdx = findIndices(data, "do()")

res = 0
while dontIdx:
    if doIdx and doIdx[-1] > dontIdx[-1]:
        res += doMult(data[doIdx[-1]:])
        data = data[:doIdx[-1]]
        doIdx.pop()
    else:
        data = data[:dontIdx[-1]]
        dontIdx.pop()
# process remaining data
res += doMult(data)
print(res)

my_file.close()
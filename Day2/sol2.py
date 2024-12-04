import os
dir = os.getcwd()

with open("input.txt", "r") as my_file:
    data = my_file.read()

data_list = data.split('\n')
arrs = [d.split(' ') for d in data_list]

def dec(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < -3 or arr[i] - arr[i - 1] > -1:
            return False
    return True

def inc(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 3 or arr[i] - arr[i - 1] < 1:
            return False
    return True
    
res = 0

for arr in arrs:
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    for i in range(len(arr)):
        val = arr.pop(i)
        if (inc(arr) or dec(arr)):
            res += 1
            break
        arr.insert(i, val)
print(res)

my_file.close()
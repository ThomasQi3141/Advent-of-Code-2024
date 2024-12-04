import os
dir = os.getcwd()

with open("input.txt", "r") as my_file:
    data = my_file.read()

data_list = data.split('\n')
arrs = [d.split(' ') for d in data_list]

def dec(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] < -3 or arr[i] - arr[i - 1] > -1:
            return 0
    return 1
def inc(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 3 or arr[i] - arr[i - 1] < 1:
            return 0
    return 1
    
res = 0

for arr in arrs:
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    if arr[1] == arr[0]:
        continue
    elif arr[1] > arr[0]:
        res += inc(arr)
    else:
        res += dec(arr)
print(res)

my_file.close()
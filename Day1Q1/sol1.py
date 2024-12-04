import os
dir = os.getcwd()

with open("input.txt", "r") as my_file:
    data = my_file.read()

data_list = data.replace('\n', ' ').split()

l1 = []
l2 = []

for i, n in enumerate(data_list):
    if i % 2 == 0:
        l1.append(int(n))
    else:
        l2.append(int(n))
        
l1.sort()
l2.sort()
res = sum(abs(l1[i] - l2[i]) for i in range(len(l1)))
print(res)


my_file.close()
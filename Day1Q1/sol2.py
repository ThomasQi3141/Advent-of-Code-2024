import os
from collections import Counter
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
        
cnt2 = Counter(l2)

res = sum(n * cnt2[n] for n in l1)

print(res)

my_file.close()
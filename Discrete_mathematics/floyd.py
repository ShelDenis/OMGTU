from pprint import pprint
from weakref import WeakKeyDictionary


ans = input('Is graph oriental? (yes/no): ')
n_r = int(input('n reber: '))
data = []
all_points = set()
for i in range(n_r):
    nums = [int(x) for x in input().split()]
    weight = int(input())
    all_points |= set(nums)
    data.append([nums, weight])
    if ans != 'yes':
        data.append([nums[::-1], weight]) 
        
v_from = int(input('From: '))
v_to = int(input('To: '))
way = [v_from, v_to]

data.sort(key=lambda x: x[0])
versh = [nums for nums, w in data]
vesa = [w for nums, w in data]
matrix = []
k = 0
for i in range(len(all_points)):
    matrix.append([])
    for j in range(len(all_points)):
        if [i + 1, j + 1] in versh:
            matrix[i].append(vesa[k])
            k += 1
        else:
            matrix[i].append(10e9)
            
for p in range(len(all_points)):
    for i in range(len(all_points)):
        if i == p:
            continue
        for j in range(len(all_points)):
            if j == p:
                continue
            if i == j:
                continue
            if matrix[i][j] > matrix[i][p] + matrix[p][j]:
                matrix[i][j] = matrix[i][p] + matrix[p][j]
                if i == v_from - 1 and j == v_to - 1:
                    way.insert(1, p + 1)
            
for line in matrix:
    for sym in line:
        if sym == 10e9:
            print('∞', end=' ')
        else:
            print(sym, end=' ')
    print()

print(' -> '.join([str(s) for s in way]))
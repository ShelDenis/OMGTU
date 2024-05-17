from copy import deepcopy

class cubAction():
    def __init__(self, A, K, S):
        self.A = A
        self.K = K
        self.S = S

cub_act_list = []

tst = 3

with open(f'Files/cub/input_s1_1{tst}.txt') as f:
    data = f.read().splitlines()

data[0] = data[0].split()
cubsize = int(list(data[0])[0])
rt_count = int(list(data[0])[1])
data[1] = data[1].split()
X0 = int(list(data[1])[0])
Y0 = int(list(data[1])[1])
Z0 = int(list(data[1])[2])
       
i = 2
while i < rt_count + 2:
    data[i] = data[i].split()
    cub_act_list.append(cubAction(list(data[i])[0],int(list(data[i])[1]),int(list(data[i])[2])))
    i += 1

#create cube
cube = [[[] for i in range(cubsize)] for j in range(cubsize)]
for z in range(cubsize):
    for y in range(cubsize):
            for x in range(cubsize):
                if z == Z0 - 1 and y == Y0 - 1 and x == X0 - 1:
                    cube[z][y].append(True)
                else:
                    cube[z][y].append(False)
#rotate cube
copy = deepcopy(cube)
for i in range(rt_count):
    copy = [list(map(list, x)) for x in copy]
    for j in range(cubsize):
        for k in range(cubsize):
            if cub_act_list[i].A == 'X':
                if cub_act_list[i].S == 1:
                    cube[k][j][cub_act_list[i].K - 1] = copy[j][cubsize - 1 - k][cub_act_list[i].K - 1]
                else:
                    cube[j][k][cub_act_list[i].K - 1] = copy[cubsize - 1 - k][j][cub_act_list[i].K - 1]
            elif cub_act_list[i].A == 'Y':
                if cub_act_list[i].S == 1:
                    cube[j][cub_act_list[i].K - 1][k] = copy[k][cub_act_list[i].K - 1][cubsize - 1 - j]
                else:
                    cube[k][cub_act_list[i].K - 1][j] = copy[cubsize - 1 - j][cub_act_list[i].K - 1][k]
            elif cub_act_list[i].A == 'Z':
                if cub_act_list[i].S == 1:
                    cube[cub_act_list[i].K - 1][j][k] = copy[cub_act_list[i].K - 1][k][cubsize - 1 - j]
                else:
                    cube[cub_act_list[i].K - 1][k][j] = copy[cub_act_list[i].K - 1][cubsize - 1 - j][k]
#seach golden element
res = [1, 1, 1]
for z in range(cubsize):
    for y in range(cubsize):
        for x in range(cubsize):
            if cube[z][y][x]:
                res[0] = x + 1
                res[1] = y + 1
                res[2] = z + 1

print(*res)
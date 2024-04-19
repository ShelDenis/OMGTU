around_dct = {1: (0, 1),
              2: (1, 1),
              3: (1, 0),
              4: (1, -1),
              5: (0, -1),
              6: (-1, -1),
              7: (-1, 0),
              8: (-1, 1)}

def get_cell(around, n):
    ar = around_dct[n]
    return (int(around[0]) + ar[0], int(around[1]) + ar[1])

def print_matrix(m):
    for k in range(1, len(m) - 1):
        print('\t'.join([str(x) for x in m[k][1:-1]]))
    

with open('Files/wave_data.txt') as f:
    f_data = f.read().splitlines()
    
matrix = [['-1'] * (len(f_data[0].split()) + 2)]

for line in f_data:
    matrix.append(['-1', *line.split(), '-1'])

matrix.append(['-1'] * (len(f_data[0].split()) + 2))


start_pos = (1, 1)
finish_pos = (1, 1)
around_n = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '0':
            start_pos = (i, j)
        if matrix[i][j] == 'f':
            finish_pos = (i, j)
            
last_cells = [start_pos]
currect_cells = []
cur_num = 1
go = True
ok = True
while go:
    for lc in last_cells:
        for i in range(1, 9):
            cx, cy = get_cell(lc, i)
            if matrix[cx][cy] != '-1':
                mat_elem = matrix[cx][cy]
                if mat_elem == 'f' or mat_elem == '-':
                    mat_elem = len(matrix) * len(matrix[0]) + 1
                mat_min = min(int(mat_elem), cur_num)
                if mat_min != matrix[cx][cy]:
                    currect_cells.append((cx, cy))
                matrix[cx][cy] = mat_min
    if (not currect_cells):
        if matrix[finish_pos[0]][finish_pos[1]] != 'f':
            print_matrix(matrix)
            around_n = matrix[finish_pos[0]][finish_pos[1]]
            break
        else:
            print("Finish no finish!")
            ok = False
            break
    last_cells = currect_cells[:]
    currect_cells = []
    cur_num += 1


back = True
around_cell = finish_pos
way = [finish_pos]
while back and ok:
    for i in range(1, 9):
        bx, by = get_cell(around_cell, i)
        bval = matrix[bx][by]
        if bval == around_n - 1:
            way.append((bx, by))
            around_cell = (bx, by)
            around_n -= 1
    if around_n == 0:
        back = False

if ok:
    way.reverse()
    print(' -> '.join(str(x) for x in way))
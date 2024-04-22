with open('Files/commi_data.txt') as f:
    f_data = f.read().splitlines()
    
matrix_const = []
matrix = []

for line in f_data:
    matrix_const.append(line.split())
    matrix.append(line.split())

dim = len(matrix)
way = []
go = True
while go:
    row_mins = []
    for line in matrix:
        line = [int(x) for x in line if x != '-']
        try:
            row_mins.append(min(line))
        except Exception:
            row_mins.append(0)
            continue
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '-':
                matrix[i][j] = int(matrix[i][j])
                matrix[i][j] -= row_mins[i]
            
    col_mins = []
    for i in range(len(matrix[0])):
        col_mins.append(min([int(line[i]) if line[i] != '-' else 10e9 for line in matrix ]))
            
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != '-':
                matrix[i][j] = int(matrix[i][j])
                matrix[i][j] -= col_mins[j]
    
    zeros_degrees = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                d_r1 = 10e9
                if j != 0:
                    d_r1 = min([elem for elem in matrix[i][:j] if elem != '-'])
                d_r2 = 10e9
                if j != len(matrix[i]) - 1:
                    d_r2 = min([elem for elem in matrix[i][j + 1:] if elem != '-'])
                d_r = min(d_r1, d_r2)
                d_c = min(matrix[k][j] for k in range(len(matrix)) if matrix[k][j] != '-' and (k, j) != (i, j))
                zeros_degrees.append([i, j, d_r + d_c])

    zeros_degrees = sorted(zeros_degrees, key=lambda x: x[-1])
    min_zero = zeros_degrees[0]
    max_zero = zeros_degrees[-1]
    way.append((max_zero[0], max_zero[1]))
    
    for i in range(len(matrix[max_zero[0]])):
        matrix[max_zero[0]][i] = '-'
    for i in range(len(matrix)):
        matrix[i][max_zero[1]] = '-'
 
    set_nums = set()
    all_nums = []
    fr = 0
    to = 0
    for elem in way:
        set_nums.add(elem[0])
        set_nums.add(elem[1])
        all_nums.append(elem[0])
        all_nums.append(elem[1])
    if len(way) != 1 and len(way) + 1 == len(set_nums):
        for num in set_nums:
            if all_nums.count(num) == 1:
                for cort in way:
                    if cort[0] == num:
                        to = num
                    elif cort[1] == num:
                        fr = num
        matrix[fr][to] == '-'
    else:
        matrix[max_zero[1]][max_zero[0]] == '-'
        
    dim -= 1
    if dim == 2:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if str(matrix[i][j]).isdigit() and matrix[i][j] != 0:
                    way.append((i, j))
                    go = False

way_seq = []
way_len = 0
while len(way) > 0:
    if not way_seq:
        way_seq.append(way[0][0])
        way_seq.append(way[0][1])
        way_len += int(matrix_const[way[0][0]][way[0][1]])
        way.pop(0)  
    else:
        for v in way:
            if v[0] == way_seq[-1]:
                way_seq.append(v[1])
                way_len += int(matrix_const[v[0]][v[1]])
                way.pop(way.index(v))
                
print(' -> '.join([str(x + 1) for x in way_seq]))
print(way_len)
    
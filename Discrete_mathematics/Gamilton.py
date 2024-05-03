with open('Files/gamil_data.txt') as f:
    f_data = f.read().splitlines()
    
matrix = [[int(x) for x in line.split()] for line in f_data]

n = len(matrix)

prev_dct = {}
cur_list = [1]
do_forming = True
last_print = ''
go = True

while go:
    if do_forming:
        smej = []
        for i in range(len(matrix[int(cur_list[-1]) - 1])):
            if matrix[int(cur_list[-1]) - 1][i] == 1:
                smej.append(i + 1)
        prev_dct['->'.join([str(x) for x in cur_list])] = [str(x) for x in smej]
    
    way = '->'.join([str(x) for x in cur_list])
    if not prev_dct[way]:
        cur_list.pop()
    elif prev_dct[way][0] not in way.split('->'):
        cur_list.append(prev_dct[way][0])
        do_forming = True
        prev_dct[way].pop(0)
    else:
        do_forming = False
        prev_dct[way].pop(0)
        
    cur_print = ''
    if len(cur_list) == n:
        if matrix[int(cur_list[-1]) - 1][0] == 1:
            cycle_list = cur_list[:]
            cycle_list.append(1)
            cur_print = ' -> '.join(str(x) for x in cycle_list) + ' - cycle'
        else:
            cur_print = ' -> '.join(str(x) for x in cur_list) + ' - way'
        
        if cur_print != last_print:
            print(cur_print)
            last_print = cur_print

    empty = True
    for val in prev_dct.values():
        if val:
            empty = False
    if empty:
        go = False
    




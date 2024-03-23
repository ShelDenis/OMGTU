def go():
    values = dct.values()
    if list(values).count('-') == len(values) - 1:
        return False
    return True


def get_len_connect(v1, v2):
    for elem in data:
        if elem[0] == [v1, v2]:
            return elem[1]
    return None


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

all_points = sorted(list(all_points))
dct = {}
mins_dct = {v_from: (0, 'start')}
for p in all_points:
    if p == v_from:
        dct[p] = 0
    else:
        dct[p] = 'inf'
        
cur_v = v_from
while go():
    for key, val in dct.items():
        if key == cur_v:
            dct[key] = '-'
        else:
            length = get_len_connect(cur_v, key)
            if length:
                if val == 'inf':
                    dct[key] = (length + mins_dct[cur_v][0], cur_v)
                elif val != '-':
                    new_len = dct[cur_v][0] + length
                    if new_len < dct[key][0]:
                        dct[key] = (new_len, cur_v)
    pred_cur_v = 0
    pred_cur_v_weight = 10e9
    for key, elem in dct.items():
        if str(elem) not in 'inf-':
            if elem[0] < pred_cur_v_weight:
                pred_cur_v = key
                pred_cur_v_weight = elem[0]

    cur_v = pred_cur_v
    mins_dct[cur_v] = dct[cur_v]
    if cur_v == v_to:
        break
    
print(f'Length = {mins_dct[v_to][0]}')

key = v_to
way = [str(v_to)]
while mins_dct[key][1] != 'start':
    way.append(str(mins_dct[key][1]))
    key = mins_dct[key][1]
way.reverse()
    
print(f'Way: {" -> ".join(way)}')
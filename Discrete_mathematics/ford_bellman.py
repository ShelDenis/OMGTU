def get_connects(vershina):
    lst = []
    for elem in data:
        if elem[0][1] == vershina:
            lst.append(elem)
    return lst

n_v = int(input('n vershin: '))
n_r = int(input('n reber: '))
is_orient = input('Orient? (yes/no) ')
data = []
cur_v = set()
for i in range(n_r):
    nums = [int(x) for x in input().split()]
    cur_v.add(nums[0])
    cur_v.add(nums[1])
    w = int(input())
    data.append((nums, w))
    if is_orient == 'no':
        data.append((nums[::-1], w))  

prev_list, cur_list = [], []
for i in range(n_v):
    prev_list.append('inf')
    cur_list.append('inf')
cur_v = sorted(list(cur_v))
o = min(cur_v)
start_v = int(input('S kakoy nachnem? '))
cur_list[start_v - o] = 0

dests = {}
for v in cur_v:
    dests[v] = 'inf'
    if v == start_v:
        dests[v] = 0

iteration = 0
go = True
no_otriz = True
while go:
    has_changed = False
    for ver in cur_v:
        if ver == start_v:
            continue
        v_list = get_connects(ver)
        if v_list:
            for elem in v_list:
                if dests[elem[0][0]] != 'inf':
                    if cur_list[ver - o] == 'inf':
                        way_len = elem[1] + dests[elem[0][0]]
                        cur_list[ver - o] = way_len, elem[0][0]
                        dests[ver] = way_len
                    else:
                        way_len = elem[1] + dests[elem[0][0]]
                        if way_len < cur_list[ver - o][0]:
                            cur_list[ver - o] = way_len, elem[0][0]
                            dests[ver - 0] = way_len
    
    if prev_list != cur_list:
        has_changed = True
        
    if has_changed and iteration == n_v:
        print('Otritsatelniy kontur!')
        no_otriz = False
        go = False
        break
    if not has_changed:
        go = False
    iteration += 1
    prev_list = cur_list[:]
     
if no_otriz:    
    print('Ways:\n')
    for v in cur_v:
        if v == start_v:
            continue
        way = []
        cont = True
        w_w = v
        while cont:
            b = cur_list[w_w - o][1]
            if b == start_v:
                print(' -> '.join([str(start_v)] + [str(x) for x in way] + [str(v)]))
                print(f'Length - {dests[v]}\n')
                cont = False
            else:
                way.insert(0, b)
                w_w = b
class Wheel:
    def __init__(self, num, zub, rot, rpm):
        self.num = num
        self.zub = zub
        self.rot = rot
        self.rpm = rpm

    def __repr__():
        return f'Wheel {num}'


shest_data = {}
come_degs = {}
connects = []
all_edges = set()

n, m = [int(x) for x in input().split()]
for i in range(n):
    num, n_zub = [int(x) for x in input().split()]
    shest_data[num] = n_zub
for i in range(m):
    c = [int(x) for x in input().split()]
    all_edges |= set(c)
    connects.append(c)
    connects.append(c[::-1])
fr, to = [int(x) for x in input().split()]
st_rotate = int(input())

queue = [[Wheel(fr, shest_data[fr], st_rotate, 1)]]
i = 0

divergents = []

while i < len(queue):
    j = len(queue[i]) - 1
    go = True
    while go:
        pairs = [pair for pair in connects if pair[0] == queue[i][j].num]
        l = 0
        while l < len(pairs):
            if pairs[l][1] in [w.num for w in queue[i]]:
                pairs.pop(l)
            else:
                l += 1

        v = round(queue[i][j].zub * queue[i][j].rpm / shest_data[pairs[0][1]], 3)
        new_wheel = Wheel(pairs[0][1], shest_data[pairs[0][1]], queue[i][j].rot * -1, v)
        queue[i].append(new_wheel)
        pairs.pop(0)
        if len(pairs) > 0:
            divergents.append(pairs[0][0])
            for k in range(1, len(pairs) + 1):
                v = round(queue[i][j].zub * queue[i][j].rpm / shest_data[pairs[0][1]], 3)
                new_wheel = Wheel(pairs[0][1], shest_data[pairs[0][1]], queue[i][j].rot * -1, v)
                queue.insert(i + k, queue[i][:j + 1])
                queue[i + k].append(new_wheel)
        if queue[i][-1].num == to:
            go = False
        j += 1
    i += 1
   
repeat_edges = []
for v in list(all_edges):
    count = 0
    for q in queue:
        if v in [el.num for el in q]:
            count += 1
    if count > 1:
        repeat_edges.append(v)
        
bad_edges = set(repeat_edges) - set(divergents)

ok = True
for bv in bad_edges:
    last_wheel = 0
    for q in queue:
        bad_v = [wh for wh in q if wh.num == bv]
        if bad_v:
            bad_v = bad_v[0]
            if last_wheel:
                if not (last_wheel.rot == bad_v.rot and last_wheel.rpm == bad_v.rpm):
                    ok = False
                    break
            last_wheel = bad_v
    if not ok:
        break
    
if not ok:
    print(-1)
else:
    print(1)
    print(queue[0][-1].rot)
    print(queue[0][-1].rpm)
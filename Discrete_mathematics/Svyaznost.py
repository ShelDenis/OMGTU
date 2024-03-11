n_r = int(input('n reber: '))
data = []
all_points = set()
for i in range(n_r):
    nums = [int(x) for x in input().split()]
    all_points |= set(nums)
    data.append(nums)
    
all_points = list(all_points)
connects = {}
for p in all_points:
    connects[p] = []
    for r in data:
        if p in r:
            connects[p].append(list(set(r).difference(set([p])))[0])

c = 0
cur_v = list(connects.keys())[0]
isp_v = [cur_v]
ind = 0

while True: # len(isp_v) < len(connects.keys())
    stop = True
    if connects[cur_v]:
        for i in range(len(connects[cur_v])):
            if connects[cur_v][i] not in isp_v:
                isp_v.append(connects[cur_v][i])
                cur_v = connects[cur_v].pop(i)
                stop = False
                break
    if stop:
        ind = len(isp_v) - 2
        end = True
        while ind >= 0:
            if connects[isp_v[ind]]:
                for i in range(len(connects[isp_v[ind]])):
                    if connects[isp_v[ind]][i] not in isp_v:
                        isp_v.append(connects[isp_v[ind]][i])
                        cur_v = connects[isp_v[ind]].pop(i)
                        end = False
            ind -= 1
        if end:
            c += 1
            ost = set(connects.keys()).difference(set(isp_v))
            if ost:
                cur_v = list(ost)[0]
                isp_v.append(cur_v)
            else:
                break
print(c)





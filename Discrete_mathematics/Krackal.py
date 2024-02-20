def in_two_sets(pair, pnts):
    inds = []
    for i in range(len(pnts)):
        if len(set(pnts[i]) & set(pair)) == 1:
            inds.append(i)
    if len(inds) == 1:
        return 0
    return inds
    

n_v = int(input('n vershin: '))
n_r = int(input('n reber: '))
data = []
for i in range(n_r):
    nums = [int(x) for x in input().split()]
    w = int(input())
    data.append((nums, w))

data.sort(key=lambda x: x[-1])

summa = 0
points = []

out = False
for p in data:
    if len(points) == 0:
        points.append(set(p[0]))
        summa += p[1]
    else:
        ok = False
        l = 0
        while l < len(points):
            if len(set(p[0]) & points[l]) == 1:
                res = in_two_sets(p[0], points)
                if res:
                    points[res[0]] |= points[res[1]]
                    points.pop(res[1])
                    summa += p[1]
                    ok = True
                else:
                    points[l] |= set(p[0])
                    summa += p[1]
                    ok = True
                    break
            elif len(set(p[0]) & points[l]) == 2:
                ok = True
                break
            l += 1
        if not ok:
            points.append(set(p[0]))
            summa += p[1]
    for po in points:
        if len(po) == n_v:
            print(f'Otvet: {summa}')
            out = True
            break
    if out:
        break





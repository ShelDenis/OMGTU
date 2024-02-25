n_v = int(input('n vershin: '))
n_r = int(input('n reber: '))
data = []
for i in range(n_r):
    nums = [int(x) for x in input().split()]
    w = int(input())
    data.append((nums, w))

data.sort(key=lambda x: x[-1])

summa = data[0][1]
points = set(data[0][0])
data.pop(0)


while len(points) < n_v:
    k = 0
    while k < len(data):
        if len(points & set(data[k][0])) == 1:
            points |= set(data[k][0])
            summa += data[k][1]
            data.pop(k)
            break
        k += 1
            
print(summa)
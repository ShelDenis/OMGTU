n_max = int(input())
count = 0

for n in range(1, n_max + 1):
    for z in range(2, 18):
        if n % (2 ** z - 1) == 0:
            count += 1
            
print(count + n_max)

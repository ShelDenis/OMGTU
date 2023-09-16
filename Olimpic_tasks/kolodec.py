k = int(input('k: '))
l = int(input('l: '))
n = int(input('n: '))
m = int(input('m: '))

print('By cicle: ')
summa = 0
for i in range(1, k + 1):
    s = 2 * (l + n + i * m)
    summa += s
print(summa)

print()
print('By formule:')
print(k * (2 * (n + l) + m * (k + 1)))


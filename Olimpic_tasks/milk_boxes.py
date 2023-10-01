# программа выводит последовательно ответы ко всем десяти тестам
for num in range(1, 11):
    with open(f'Files/milk/input{num}.txt') as f:
        data = f.read().splitlines()

    n = int(data[0])
    min_num, min_price = 0, 10e9
    for i in range(1, n + 1):
        x1, y1, z1, x2, y2, z2, c1, c2 = list(map(float, data[i].split()))
        v1, v2 = x1 * y1 * z1, x2 * y2 * z2
        s1, s2 = 2 * (x1 * y1 + x1 * z1 + y1 * z1), 2 * (x2 * y2 + x2 * z2 + y2 * z2)
        v0, s0 = v2 / v1, s2 / s1
        milk_price = (c2 - s0 * c1) / (v2 - s0 * v1) * 1000
        if milk_price < min_price:
            min_price = milk_price
            min_num = i

    print(f'Test {num}:\n', min_num, f'{min_price:.2f}\n')
    #with open(f'Files/milk/output{num}.txt') as f:
        #print(f.read())
        #print()   # При выводе данных сверяется информация, полученная в результате программы с результатом в output.txt
    
    
    



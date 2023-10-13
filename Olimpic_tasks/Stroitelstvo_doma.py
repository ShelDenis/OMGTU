for i in range(1, 15):
    num = '0' + str(i) if len(str(i)) == 1 else str(i) 
    with open(f'Files/house/input_s1_{num}.txt') as f:
        data = f.read()
        data = [int(x) for x in data.split()]
    
    x, y, l, c1, c2, c3, c4, c5, c6 = data
    quantity = 0
    trash = 0
    p = 2 * (x + y)

    wall_ostatok = l - max(x, y)
    wall_base = l

    if l > p:
        # вывоз лишнего на свалку
        trash = (l - p) * (c2 + c6)
        wall_base -= (l - p)
        wall_ostatok -= (l - p)
        l = p
    if wall_ostatok <= 0:
        # если стену дешевле не разбирать
        if c1 < (c2 + c4 + c5 + c6):
            # если дешевле отремонтировать 
            if c1 < (c2 + c3):
                quantity = wall_base * c1 + (p - l) * (c4 + c5)
            # если дешевле построить из переработанного материала
            else:
                quantity = wall_base * (c2 + c3) + (p - l) * (c4 + c5)
        # если стену дешевле разобрать
        else:
            quantity = wall_base * (c2 + c6) + p * (c4 + c5)
    else:
        # если стену дешевле не разбирать
        if c1 < (c2 + c4 + c5 + c6):
            if c3 < (c4 + c5 + c6):
                # если дешевле восстановить
                if c1 < (c2 + c3):
                    # если дешевле отремонтировать
                    quantity = (wall_base - wall_ostatok) * c1 + wall_ostatok * (c2 + c3) + (p - l) * (c4 + c5)
                else:
                    # если дешевле снести и построить из старого материала
                    quantity = (wall_base - wall_ostatok) * (c2 + c3) + wall_ostatok * (c2 + c3) + (p - l) * (c4 + c5)
            else:
                if c1 < (c2 + c3):
                    # если дешевле отремонтировать без старого материала
                    quantity = (wall_base - wall_ostatok) * c1 + wall_ostatok * (c2 + c6) + (p - l + wall_ostatok) * (c4 + c5)
                else:
                    # если дешевле переработать старую стену
                    quantity = (wall_base - wall_ostatok) * (c2 + c3) + wall_ostatok * (c2 + c6) + (p - l + wall_ostatok) * (c4 + c5)
        else:
            # постройка дома из новых стен
            quantity = wall_base * (c2 + c6) + p * (c4 + c5)
       
    print(quantity + trash)
    with open(f'Files/house/output_s1_{num}.txt') as f:
        print(f.read())
        print()
        
        
    

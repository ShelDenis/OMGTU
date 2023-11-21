for num in range(1, 15):
    with open(f'Files/obmen/input{num}.txt') as f:
        data = f.read().splitlines()
    

    n_money_system_1, *c1 = [int(x) for x in data[0].split()]
    n_unlucky_1, *unlucky1 = [int(x) for x in data[1].split()]

    n_money_system_2, *c2 = [int(x) for x in data[2].split()]
    n_unlucky_2, *unlucky2 = [int(x) for x in data[3].split()]

    money_parts = [int(x) for x in data[4].split()]

    c1.append(1)  #последний коэф = 1
    c2.append(1)  #последний коэф = 1

    #преобразуем деньги первой системы в минимальные единицы
    quantity = 0
    tmp = 0
    unh = 0
    i = 1
    while(i <= len(money_parts)):
        tmp = money_parts[-i]
        j = 0
        unh = 0
        while (j < len(unlucky1)):
            if tmp > unlucky1[j]:
                unh += 1
            j += 1
        tmp -= unh
        j = i
        tmp_c = 1
        while(j > 0):
            tmp_c *= c1[-j]
            j -= 1
        quantity += tmp * tmp_c
        i += 1

    #преобразуем минимальные единицы во вторую денежную систему
    i = 0
    money_2 = []
    while(i < len(c2)):
        j = i
        tmp_c = 1
        while(j < len(c2)):
            tmp_c *= c2[j]
            j += 1
        m = quantity // tmp_c

        n_clear_money = 0
        res = 0
        while(n_clear_money < m):
            flag = False
            j = 0
            while (j < len(unlucky2)):
                if res == unlucky2[j]:
                    break
                j += 1
            if j == len(unlucky2):
                flag = True
            res += 1
            if flag:
                n_clear_money += 1
 
        tmp = m
        # #проверяем полученное число счастливое?
        flag = False
        while(flag == False):
            j = 0
            while (j < len(unlucky2)):
                if res == unlucky2[j]:
                    res += 1
                    break;
            
                j += 1
            if j == len(unlucky2):
                flag = True

        money_2.append(str(res))
        quantity -= tmp * tmp_c
        i += 1

    print(' '.join(money_2))
    with open(f'Files/obmen/output{num}.txt') as f:
        print(f.read())
        print()
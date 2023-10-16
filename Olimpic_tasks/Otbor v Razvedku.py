n = int(input())
powers_of_2 = [2 ** m for m in range(1, 500)]

if n in powers_of_2:
    print(0)
elif n % 6 == 0 and n // 3 in powers_of_2:
    print(n // 3)
else:
    for i in range(len(powers_of_2) - 1):
        if powers_of_2[i] < n < powers_of_2[i + 1]:
            sr_ar = (powers_of_2[i] + powers_of_2[i + 1]) // 2
            print((sr_ar // 3) - abs(sr_ar - n))
            break




n = 1
with open(f'Files/poison/input{n}.txt') as f:
    data = f.read().splitlines()
    
spells = {
    'MIX': 'MX',
    'WATER': 'WT',
    'DUST': 'DT',
    'FIRE': 'FR'
    }

magic_products = []
for line in data:
    line = line.split()
    spell, ingridients = line[0], line[1:]
    kayma = spells[spell]
    long_spell = ''
    for ing in ingridients:
        if ing.isdigit():
            long_spell += magic_products[int(ing) - 1]
        else:
            long_spell += ing
    magic_products.append(kayma + long_spell + kayma[::-1])
    
print(magic_products[-1])

with open(f'Files/poison/output{n}.txt') as f:
    fr = f.read()
    print(fr)
    if magic_products[-1] == fr:
        print('Ok!')
    else:
        print('Ko!')
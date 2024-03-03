def check(idishnik):
    if idishnik in dct_rel.keys():
        return True
    return False
          

dct_rel = {}
dct_names = {}
k = 0
boss = ''
s = input()

while s != 'END':
    ide = s[:4]
    if k % 2 == 0:
        if ide not in dct_rel.keys():
            dct_rel[ide] = []
        boss = ide
    else:
        dct_rel[boss].append(ide)
    k += 1
    k %= 2;
    if ' ' in s:
        ide, name = s[:4], s[5:]
        if ide in dct_names.keys():
            if dct_names[ide] == '':
                dct_names[ide] = name
        else:
            dct_names[ide] = name
    else:
        if ide not in dct_names.keys():
            dct_names[ide] = ''
    s = input()

queue = []
ok = True
search = input()
if len(set(search) | set('0123456789')) == 10:
    if check(search):
        queue.extend(dct_rel[search])
    else:
        print('NO')
        ok = False
else:
    for k, v in dct_names.items():
        if v == search:
            if check(k):
                queue.extend(dct_rel[k])
            else:
                print('NO')
                ok = False
if ok:
    i = 0
    while i < len(queue):
        if check(queue[i]):
            queue.extend(dct_rel[queue[i]])
        i += 1
    queue.sort()
    for slave in queue:
        if dct_names[slave]:
            print(slave, dct_names[slave])
        else:
            print(slave, "Unknown Name")
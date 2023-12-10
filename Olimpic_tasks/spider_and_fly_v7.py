import math

fileNum = 9;

with open(f'Files/spider/input_s1_1{fileNum}.txt') as f:
    data = f.read().splitlines()
    
lstRes = []

a, b, c = [int(x) for x in data[0].split()]
sx, sy, sz = [int(x) for x in data[1].split()]
fx, fy, fz = [int(x) for x in data[2].split()]

tsx, tsy, tsz = sx, sy, sz
tfx, tfy, tfz = fx, fy, fz

#решение с использованием развертки относительно XZ
#относительно простая развертка без "хвоста"
#по оси X
if sx == 0:
    sx -= sy
if fx == 0:
    fx -= fy
if sx == a:
    sx += sy
if fx == a:
    fx += fy
#по оси Z
if sz == 0:
    sz -= sy
if fz == 0:
    fz -= fy
if sz == c:
    sz += sy
if fz == c:
    fz += fy

sx_left = sx
fx_left = fx
sz_left = sz
fz_left = fz

sx_top = sx
fx_top = fx
sz_top = sz
fz_top = fz

sx_right = sx
fx_right = fx
sz_right = sz
fz_right = fz

sx_bottom = sx
fx_bottom = fx
sz_bottom = sz
fz_bottom = fz

#проверяем есть ли точки на противоположной грани XZ
if sy == b or fy == b:
    #лежат в одной плоскости
    if sy == b and fy == b:
        res = math.sqrt( ((sx - fx) ** 2) + ((sz - fz) ** 2) )
        lstRes.append(res)
    else:
        #хвост слева
        if sy == b:
            sx_left = - (sx + b)
        if fy == b:
            fx_left = - (fx + b)
        res = math.sqrt( ((sx_left - fx_left) ** 2) + ((sz_left - fz_left) ** 2) )
        lstRes.append(res)
        #хвост сверху
        if sy == b:
            sz_top = c + b + (c - sz)
        if fy == b:
            fz_top = c + b + (c - fz)
        res = math.sqrt( ((sx_top - fx_top) ** 2) + ((sz_top - fz_top) ** 2) )
        lstRes.append(res)
        #хвост справо
        if sy == b:
            sx_right = a + b + (a - sx)
        if fy == b:
            fx_right = a + b + (a - fx)
        res = math.sqrt( ((sx_right - fx_right) ** 2) + ((sz_right - fz_right) ** 2) )
        lstRes.append(res)
        #хвост снизу
        if sy == b:
            sz_bottom = - (sz + b)
        if fy == b:
            fz_bottom = - (fz + b)
        res = math.sqrt( ((sx_bottom - fx_bottom) ** 2) + ((sz_bottom - fz_bottom) ** 2) )
        lstRes.append(res)
      
else:
    res = math.sqrt( ((sx - fx) ** 2) + ((sz - fz) ** 2) )
    lstRes.append(res)
      
sx, sy, sz = tsx, tsy, tsz
fx, fy, fz = tfx, tfy, tfz

#решение с использованием развертки относительно XY
#относительно простая развертка без "хвоста"
#по оси X
if sx == 0:
    sx -= sz
if fx == 0:
    fx -= fz
if sx == a:
    sx += sz
if fx == a:
    fx += fz
#по оси Y
if sy == 0:
    sy -= sz
if fy == 0:
    fy -= fz
if sy == b:
    sy += sz
if fy == b:
    fy += fz
 
sx_left = sx
fx_left = fx
sy_left = sy
fy_left = fy

sx_top = sx
fx_top = fx
sy_top = sy
fy_top = fy

sx_right = sx
fx_right = fx
sy_right = sy
fy_right = fy

sx_bottom = sx
fx_bottom = fx
sy_bottom = sy
fy_bottom = fy

#проверяем есть ли точки на противоположной грани XY
if sz == c or fz == c:
    #лежат в одной плоскости
    if sz == c and fz == c:
        res = math.sqrt( ((sx - fx) ** 2) + ((sy - fy) ** 2) )
        lstRes.append(res)
    else:
        #хвост слева
        if sz == c:
            sx_left = - (sx + c)
        if fz == c:
            fx_left = - (fx + c)
        res = math.sqrt( ((sx_left - fx_left) ** 2) + ((sy_left - fy_left) ** 2) )
        lstRes.append(res)
        #хвост сверху
        if sz == c:
            sy_top = c + b + (b - sy)
        if fz == c:
            fy_top = c + b + (b - fy)
        res = math.sqrt( ((sx_top - fx_top) ** 2) + ((sy_top - fy_top) ** 2) )
        lstRes.append(res)
        #хвост справо
        if sz == c:
            sx_right = a + c + (a - sx)
        if fz == c:
            fx_right = a + c + (a - fx)
        res = math.sqrt( ((sx_right - fx_right) ** 2) + ((sy_right - fy_right) ** 2) )
        lstRes.append(res)
        #хвост снизу
        if sz == c:
            sy_bottom = - (sy + c)
        if fz == c:
            fy_bottom = - (fy + c)
        res = math.sqrt( ((sx_bottom - fx_bottom) ** 2) + ((sy_bottom - fy_bottom) ** 2) )
        lstRes.append(res)
      
else:
    res = math.sqrt( ((sx - fx) ** 2) + ((sy - fy) ** 2) )
    lstRes.append(res)

res = min(lstRes)
print(f'{res:.3f}')
with open(f'Files/spider/output_s1_1{fileNum}.txt') as f:
    print(f.read())




class Vertex:
    def __init__(self, num, c, vfr):
        self.num = num
        self.c = c
        self.vfr = vfr

class Arc:
    def __init__(self, fr, to, c, f):
        self.fr = fr
        self.to = to
        self.c = c
        self.f = f
        
def get_v_by_num(n):
    return [x for x in vertexs if x.num == n][0]

def get_v_index_in_list(n):
    return [i for i in range(len(vertexs)) if vertexs[i].num == n][0]

def get_arc_ind(f, t):
    return [i for i in range(len(arcs)) if arcs[i].fr == f and arcs[i].to == t][0]

vertexs = []
arcs = []

n_versh = int(input())
n_r = int(input())
for i in range(1, n_versh + 1):
    print(f'Vertex {i}')
    number = int(input())
    vertexs.append(Vertex(number, 0, None))
    
for i in range(1, n_r + 1):
    print(f'Arc {i}')
    v_from, v_to, c = [int(x) for x in input().split()]
    arcs.append(Arc(v_from, v_to, c, 0))
    
start = int(input())
finish = int(input())

way = [start]
summa = 0
min_c = 10e9
cur_v = get_v_by_num(start)
negative_arcs = []
bad_vs = []
koef = 1
go = True
while go:
    inc_arcs = [a for a in arcs if a.fr == cur_v.num and a.to not in bad_vs]
    max_arc = sorted(inc_arcs, key=lambda x: x.c)[-1]
    if max_arc.c != 0:
        index = get_v_index_in_list(max_arc.to)
        min_c = min(min_c, max_arc.c)
        vertexs[index].mark = max_arc.c
        vertexs[index].vfr = max_arc.fr
        cur_v = vertexs[index]
        way.append(cur_v.num)
        if cur_v.num == finish:
            for k in range(len(way) - 1, 0, -1):
                ver_ver = ver_to, ver_fr = way[k], way[k - 1]
                if ver_ver in [(a.fr, a.to) for a in negative_arcs]:
                    koef = -1
                if koef == 1:
                    a_ind = get_arc_ind(ver_fr, ver_to)
                else:
                    a_ind = get_arc_ind(ver_to, ver_fr)
                arcs[a_ind].c -= (min_c * koef)
                arcs[a_ind].f += (min_c * koef)
                koef = 1
            cur_v = get_v_by_num(start)
            way = [start]
            summa += min_c
            min_c = 10e9          
    
    else:
        back_arc = [a for a in arcs if a.to == cur_v.num and a.fr != way[way.index(cur_v.num) - 1]][0]
        way.append(back_arc.fr)
        bad_vs.append(back_arc.to)
        min_c = min(min_c, back_arc.f)
        negative_arcs.append(back_arc)
        cur_v = get_v_by_num(back_arc.fr)
        
    st_arcs = [a for a in arcs if a.fr == start]
    fn_arcs = [a for a in arcs if a.to == finish]
    ok1 = False
    ok2 = False
    for a in st_arcs:
        if a.c != 0:
            ok1 = True
    for a in fn_arcs:
        if a.c != 0:
            ok2 = True
    ok = ok1 and ok2
    
    go = ok
            
    
print(summa)




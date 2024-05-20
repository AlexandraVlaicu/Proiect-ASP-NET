class NodArbore:
    def __init__(self,  informatie, parinte=None):
        self.informatie = informatie
        self.parinte = parinte


    def drumRadacina(self):
        nod=self
        l=[nod]
        while nod.parinte:
            nod=nod.parinte
            l.insert(0, nod)
        return l

    def oNod):
        nod=self
        if infoNod == nod.informatie:
            return True
        while nod.parinte:
            nod=nod.parinte
            if infoNod==nod.informatie:
                return True

        return False


    def __str__(self):
        return str(self.informatie)

    #"c (a->b->c)"
    def __repr__(self):
        return f"{self.informatie} ({'->'.join(map(str,self.drumRadacina()))})"

class Graf:
    def __init__(self, matr, start, scopuri):
        self.matr = matr
        self.start = start
        self.scopuri = scopuri

    def  scop(self, informatieNod):
        return informatieNod in self.scopuri

    def succesori(self, nod):
        lSuccesori=[]
        for infoSuccesor in range(len(self.matr)):
            if self.matr[nod.informatie][infoSuccesor]==1 and not nod.inDrum(infoSuccesor):
                lSuccesori.append(NodArbore(infoSuccesor, nod))
        return  lSuccesori

def breadthFirst(gr, nsol=3):
    coada=[NodArbore(gr.start)]
    while coada:
        nodCurent=coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            nsol-=1
            if nsol==0:
                return
        coada+=gr.succesori(nodCurent)


def depthFirstNerecursiv(gr, nsol=3):
    stiva=[NodArbore(gr.start)]
    while stiva:
        nodCurent=stiva.pop()
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            nsol-=1
            if nsol==0:
                return
        stiva+=gr.succesori(nodCurent)[::-1]

def depthFirstRecursiv(gr, nsol=3):
    df(NodArbore(gr.start), gr, nsol)

def df(nodCurent, gr, nsol):
    if gr.scop(nodCurent.informatie):
        print(repr(nodCurent))
        nsol -= 1
        if nsol == 0:
            return nsol
    for s in gr.succesori(nodCurent):
        nsol=df(s, gr, nsol)
        if nsol == 0:
            return nsol
    return nsol





m = [
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]


start = 0
scopuri = [5, 9]
gr=Graf(m, start, scopuri)
print("breadthFirst")
breadthFirst(gr, 4)
print("depthFirstNerecursiv")
depthFirstNerecursiv(gr, 4)
print("depthFirstRecursiv")
depthFirstRecursiv(gr, 4)

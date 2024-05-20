
class NodArbore:
    def __init__(self,  informatie, g=0, h=0,parinte=None):
        self.informatie = informatie
        self.parinte = parinte
        self.g=g
        self.h=h
        self.f=g+h

    def __eq__(self,elem):
        return (self.f, self.g)==(elem.f,elem.g)

    def __lt__(self,elem):
        return self.f < elem.f or (self.f == elem.f and self.h<elem.h)

    def drumRadacina(self):
        nod=self
        l=[nod]
        while nod.parinte:
            nod=nod.parinte
            l.insert(0, nod)
        return l

    def inDrum(self,infoNod):
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
        return f"{self.informatie} cost:{self.g} ({'->'.join(map(str,self.drumRadacina()))})"


class Graf:
    def __init__(self,  start, scopuri):

        self.start=start
        self.scopuri=scopuri

    def scop(self, informatieNod):
        return informatieNod in self.scopuri

    def estimeaza_h(self,infoNod):
        return (infoNod[0]+infoNod[1])/Graf.M

    # (numar_misionari_mal_initial, numar_canibali_mal_initial, mal_curent)
    #mal initial = 1; mal final =0
    #mal curent= mal cu barca
    def succesori(self, nod):

        def testConditie(m, c):
            return m==0 or m>=c

        lSuccesori=[]
        if nod.informatie[2]==1:
            misMalCurent=nod.informatie[0]
            canMalCurent=nod.informatie[1]
            misMalOpus=Graf.N-nod.informatie[0]
            canMalOpus=Graf.N-nod.informatie[1]
        else:
            misMalOpus=nod.informatie[0]
            canMalOpus=nod.informatie[1]
            misMalCurent=Graf.N-nod.informatie[0]
            canMalCurent=Graf.N-nod.informatie[1]
        maxMisBarca=min(misMalCurent,Graf.M)
        for mb in range(maxMisBarca+1):
            if mb==0:
                minCanBarca=1
                maxCanBarca = min(canMalCurent, Graf.M)
            else:
                minCanBarca = 0
                maxCanBarca = min(canMalCurent, Graf.M-mb, mb)
            for cb in range(minCanBarca, maxCanBarca + 1):
                misMalCurentNou=misMalCurent-mb
                canMalCurentNou = canMalCurent - cb
                misMalOpusNou=misMalOpus+mb
                canMalOpusNou=canMalOpus+cb
                if not testConditie(misMalCurentNou,canMalCurentNou):
                    continue
                if not testConditie(misMalOpusNou,canMalOpusNou):
                    continue
                if nod.informatie[2]==1:
                    infoSuccesor=(misMalCurentNou,canMalCurentNou,0)
                else:
                    infoSuccesor = (misMalOpusNou, canMalOpusNou, 1)

                if not nod.inDrum(infoSuccesor):
                    lSuccesori.append(NodArbore(
                        infoSuccesor,
                        nod.g + 1,
                        self.estimeaza_h(infoSuccesor),
                        nod))
        return lSuccesori


def breadthFirst(gr, nsol=2):
    coada=[NodArbore(gr.start)]
    while coada:
        nodCurent=coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            nsol-=1
            if nsol==0:
                return
        coada+=gr.succesori(nodCurent)

def aStarSolMultiple(gr, nsol=3):
    coada=[NodArbore(gr.start)]
    while coada:
        nodCurent=coada.pop(0)
        if gr.scop(nodCurent.informatie):
            print(repr(nodCurent))
            nsol-=1
            if nsol==0:
                return
        coada+=gr.succesori(nodCurent)
        coada.sort()



f=open("input.txt","r")
[Graf.N,Graf.M]=f.readline().strip().split()
Graf.N=int(Graf.N)
Graf.M=int(Graf.M)

#(numar_misionari_mal_initial, numar_canibali_mal_initial, mal_curent)
#malCurent = 1 malul initial; 0 malul final
start = (Graf.N, Graf.N, 1)
scopuri = [(0,0,0)]


gr=Graf(start,scopuri)
aStarSolMultiple(gr, nsol=3)
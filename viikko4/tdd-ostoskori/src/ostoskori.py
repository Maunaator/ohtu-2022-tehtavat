from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.sisalto = {}

    def tavaroita_korissa(self):
        lukumaarat = map(lambda ostos: ostos.lukumaara(), self.sisalto.values())
        return sum(lukumaarat)

    def hinta(self):
        hinnat = map(lambda ostos: ostos.hinta(), self.sisalto.values())
        return sum(hinnat)

    def lisaa_tuote(self, lisattava: Tuote):
        if self.sisalto.get(lisattava):
            self.sisalto.get(lisattava).muuta_lukumaaraa(1)
        else:
            self.sisalto[lisattava] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        if self.sisalto.get(poistettava):
            self.sisalto.get(poistettava).muuta_lukumaaraa(-1)
            if self.sisalto.get(poistettava).lukumaara() <= 0:
                self.sisalto.pop(poistettava)

    def tyhjenna(self):
        self.sisalto.clear()

    def ostokset(self):
        return list(self.sisalto.values())
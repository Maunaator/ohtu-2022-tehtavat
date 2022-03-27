
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        
        if type(kapasiteetti) != int or kapasiteetti < 0:
            raise Exception("Virheellinen kapasiteetti")  
        
        if type(kasvatuskoko) != int or kasvatuskoko < 0:
            raise Exception("Virheellinen kasvatuskoko")
        #testit menevät kyllä läpi ilmankin, mutta jätetään tarkastukset
            
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.muisti = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.muisti
    # vähän kyseenalaista onko tehtävän hengen mukaista tehdä näin
        
    def lisaa(self, n):
        if not self.kuuluu(n):
            self.muisti[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.muisti):
                self.muisti = self.muisti + [0] * self.kasvatuskoko
            return True
        else:
            return False
        
    def poista(self, n):

        for i in range(0, self.alkioiden_lkm):
            if n == self.muisti[i]:
                self.muisti = self.muisti[0:i] + self.muisti[i+1:len(self.muisti)]
                self.alkioiden_lkm += -1
                return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.muisti[0:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.muisti[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.muisti[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.muisti[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos

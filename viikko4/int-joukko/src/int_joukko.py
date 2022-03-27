
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        
        if type(kapasiteetti) != int or kapasiteetti < 0:
            raise Exception("Virheellinen kapasiteetti")  
        
        if type(kasvatuskoko) != int or kasvatuskoko < 0:
            raise Exception("Virheellinen kasvatuskoko")
        #testit menevät kyllä läpi ilmankin, mutta jätetään tarkastukset
            
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.joukko = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.joukko
    # vähän kyseenalaista onko tehtävän hengen mukaista tehdä näin
        
    def lisaa(self, n):
        if not self.kuuluu(n):
            self.joukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.joukko):
                self.joukko = self.joukko + [0] * self.kasvatuskoko
            return True
        else:
            return False
        
    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.joukko[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.joukko[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.joukko[j]
                self.joukko[j] = self.joukko[j + 1]
                self.joukko[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.joukko[0:self.alkioiden_lkm]

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
            return "{" + str(self.joukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.joukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.joukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos

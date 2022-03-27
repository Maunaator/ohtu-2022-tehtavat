
class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        
        if type(kapasiteetti) != int or kapasiteetti < 1:
            raise Exception("Virheellinen kapasiteetti")  
        
        if type(kasvatuskoko) != int or kasvatuskoko < 1:
            raise Exception("Virheellinen kasvatuskoko")
        #testit menevät kyllä läpi ilmankin, alle 1 arvot johtaisivat erikoiseen toimintaan
        #periaatteessa pythonin listan kanssa kapasiteetista ja kasvatuskoosta ei tarvitsisi pitää huolta
            
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.muisti = [0] * self.kapasiteetti
        self.alkioita = 0

    def kuuluu(self, n):
        return n in self.muisti
    # vähän kyseenalaista onko tehtävän hengen mukaista tehdä näin
        
    def lisaa(self, n):
        if not self.kuuluu(n):
            self.muisti[self.alkioita] = n
            self.alkioita += 1

            if self.alkioita == len(self.muisti):
                self.muisti = self.muisti + [0] * self.kasvatuskoko
            return True
        else:
            return False
        
    def poista(self, n):
        for i in range(0, self.alkioita):
            if n == self.muisti[i]:
                self.muisti.pop(i)
                self.alkioita += -1
                return True
        return False

    def mahtavuus(self):
        return self.alkioita

    def to_int_list(self):
        return self.muisti[0:self.alkioita]

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
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    x.lisaa(b_taulu[j])

        return x

    @staticmethod
    def erotus(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.poista(b_taulu[i])

        return x

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"

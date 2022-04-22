class Komento:
    def __init__(self, logiikka, input=None):
        self.logiikka = logiikka
        self.input = input

class Summa(Komento):
    def __init__(self, logiikka, input):
        super().__init__(logiikka, input)

    def suorita(self):
        self.logiikka.aseta_arvo(
            self.logiikka.nykyinen_arvo() + self.input())

class Erotus(Komento):
    def __init__(self, logiikka, input):
        super().__init__(logiikka, input)

    def suorita(self):
        self.logiikka.aseta_arvo(
            self.logiikka.nykyinen_arvo() - self.input())

class Nollaus(Komento):
    def __init__(self, logiikka):
        super().__init__(logiikka)

    def suorita(self):
        self.logiikka.aseta_arvo(0)

class Kumoa(Komento):
    def __init__(self, logiikka):
        super().__init__(logiikka)

    def suorita(self):
        self.logiikka.kumoa()


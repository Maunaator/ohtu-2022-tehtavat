class Komento:
    def __init__(self, logiikka, input):
        self.logiikka = logiikka
        self.input = input

    def hae_input(self):
        return self.input()

class Summa(Komento):
    def __init__(self, logiikka, input):
        super().__init__(logiikka, input)

    def suorita(self):
        self.logiikka.plus(self.hae_input())

class Erotus(Komento):
    def __init__(self, logiikka, input):
        super().__init__(logiikka, input)

    def suorita(self):
        self.logiikka.miinus(self.hae_input())

class Nollaus(Komento):
    def __init__(self, logiikka, input):
        super().__init__(logiikka, input)

    def suorita(self):
        self.logiikka.nollaa()

class Kumoa(Komento):
    def __init__(self, logiikka, input):
        super().__init__(logiikka, input)

    def suorita(self):
        self.logiikka.kumoa()


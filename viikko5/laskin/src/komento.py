class Komento:
    def __init__(self, muisti, input=None):
        self.muisti = muisti
        self.input = input

class Summa(Komento):
    def __init__(self, muisti, input):
        super().__init__(muisti, input)

    def suorita(self):
        self.muisti.aseta_arvo(
            self.muisti.nykyinen_arvo() + self.input())

class Erotus(Komento):
    def __init__(self, muisti, input):
        super().__init__(muisti, input)

    def suorita(self):
        self.muisti.aseta_arvo(
            self.muisti.nykyinen_arvo() - self.input())

class Nollaus(Komento):
    def __init__(self, muisti):
        super().__init__(muisti)

    def suorita(self):
        self.muisti.aseta_arvo(0)

class Kumoa(Komento):
    def __init__(self, muisti):
        super().__init__(muisti)

    def suorita(self):
        self.muisti.kumoa()


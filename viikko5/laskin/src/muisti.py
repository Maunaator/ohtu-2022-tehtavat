class Muisti:
    def __init__(self, tulos=None):
        self.tulos = tulos or [0]

    def nykyinen_arvo(self):
        return self.tulos[-1]

    def aseta_arvo(self, arvo):
        self.tulos.append(arvo)

    def kumoa(self):
        if len(self.tulos) >1:
            self.tulos.pop()

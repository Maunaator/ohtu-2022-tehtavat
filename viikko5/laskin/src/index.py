from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from muisti import Muisti


def main():
    muisti = Muisti()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(muisti, window)
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()

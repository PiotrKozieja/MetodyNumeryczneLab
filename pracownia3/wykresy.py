"""Klasa realizujaca wykresy"""

from matplotlib import pyplot as plt
import numpy as np

class Wykresy:

    def __init__(self, n = 2000):
        """Konstruktor"""
        self.n = n              # liczba danych

    def badaj_zbieznosc(
        self, tytul, opis_OY, dane1, opis1,
        dane2 = None, opis2 = None, dane3 = None, opis3 = None
    ):
        """Wykres jednej, dwóch lub trzech serii danych
            - pierwsza seria - czerwona, druga - niebieska, trzecia - zielona
            - nazwa - opis na osi OY"""
        # tworzymy wykres
        plt.figure(facecolor = "white")
        seria1 = plt.plot(dane1, "ro")
        plt.title(tytul)
        # jezeli nie ma nawet jednej serii danych - niczego nie rysujemy
        if len(dane1) < 2:
            return 0
        dane_max = max(dane1)
        dane_min = min(dane1)
        if dane2:
            dane_max = max(dane_max, max(dane2))
            dane_min = min(dane_min, min(dane2))
            seria2 = plt.plot(dane2, "bo")
        if dane3:
            dane_max = max(dane_max, max(dane3))
            dane_min = min(dane_min, min(dane3))
            seria3 = plt.plot(dane3, "go")
        delta = 0.05*(dane_max-dane_min)
        y_min = dane_min - delta
        y_max = dane_max + delta
        plt.ylim(y_min, y_max)
        plt.xlabel("Numer iteracji")
        plt.ylabel(opis_OY)
        plt.margins(0.1)
        local = "upper right"
        if not dane3:
            if not dane2:
                plt.legend(seria1, [opis1], loc = local)
            else:
                plt.legend(seria1 + seria2, [opis1, opis2], loc = local)
        elif not dane2:
            plt.legend(seria1 + seria3, [opis1, opis3], loc = local)
        else:
            plt.legend(seria1 + seria2 + seria3, [opis1, opis2, opis3], loc = local)
        plt.grid(True)
        plt.show()
        
    def wykres_wielomianow(self, f, a, b, opis):
        """Metoda rysujaca wykres wielomianu f i jej pochodnych
            na zadanym przedziale [a, b]"""
        # tworzymy tablice argumentow, by krzywe byla gladka
        # jezeli mamy pusty przedzial - niczego nie rysujemy
        if a == b:
            return 0
        else:
            x = np.arange(a, b, 1.0*(b-a)/self.n)
        #obliczamy pochodne
        poch = f.pochodna()
        druga_poch = poch.pochodna()
        # obliczamy wartosci
        y0 = f.wartosc(x)
        y1 = poch.wartosc(x)
        y2 = druga_poch.wartosc(x)
        # tworzymy wykres
        plt.figure(facecolor = "white")
        seria1 = plt.plot(x, y0, "r-")
        seria2 = plt.plot(x, y1, "g-")
        seria3 = plt.plot(x, y2, "b-")
        plt.title(opis)
        # okreslamy zakres osi OX
        delta = abs(b-a)*0.05
        plt.xlim(a-delta, b+delta)
        # okreslamy zakres osi OY
        f_min = min(min(y0), min(y1), min(y2))
        f_max = max(max(y0), max(y1), max(y2))
        delta = 0.05*(f_max-f_min)
        y_min = f_min - delta
        y_max = f_max + delta
        plt.ylim(y_min, y_max)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.margins(0.1)
        plt.legend(seria1+seria2+seria3, ["f(x)", "f'(x)", "f''(x)"], loc = "upper left")
        plt.grid(True)
        plt.show()
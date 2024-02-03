"""Przyklad zastosowania metod przyblizonych"""

import funkcja, wykresy
import metodatrapezow, metodaparabol, metodanewtona

class Zadanie2:
  
    def __init__(self):
        """Konstruktor klasy"""
        # okreslamy funkcje
        self.f = funkcja.Funkcja()
        # okreslamy krance przedzialu
        self.a = -2.0
        self.b = 4.0
        # okreslamy parametry eksperymentu
        self.n = 100
        self.epsilon = 1.0e-6
    
    def porownaj(self, war_stopu):
        """Metoda porownujaca metody calkowania,
            parametr war_stopu okresla kryterium stopu:
            0 - zadana maksymalna liczba podprzedzialow
            1 - iteracje zatrzymywane, gdy dwa kolejne przyblizenia
                dostatecznie blisko siebie"""
        # metoda trapezow
        # print("Metoda trapezow")
        # test1 = metodatrapezow.MetodaTrapezow(
        #     funkcja = self.f,
        #     lewy_kp = self.a,
        #     prawy_kp = self.b)
        # if (war_stopu == 0):
        #     test1.iteruj(iteracje = self.n, wyswietlaj = 1)
        # else:
        #     test1.iteruj_roznica(eps = self.epsilon, wyswietlaj = 1)
        # # metoda parabol
        # print("-"*30)
        print("Metoda parabol")
        test2 = metodaparabol.MetodaParabol(
            funkcja = self.f,
            lewy_kp = self.a,
            prawy_kp = self.b)
        test2.iteruj_roznica(eps = self.epsilon, wyswietlaj = 1)
        # metoda 3/8 Newtona
        print("-"*30)
        print("Metoda 3/8 Newtona")
        test3 = metodanewtona.MetodaNewtona(
            funkcja = self.f,
            lewy_kp = self.a,
            prawy_kp = self.b)
        test3.iteruj_roznica(eps = self.epsilon, wyswietlaj = 1)
        # obrazujemy zbieznosc tych metod na wykresie
        wykres1 = wykresy.Wykresy()
        wykres1.badaj_zbieznosc(
            tytul = "Metody calkowania",
            opis_OY = "Przyblizenia calki",
            # dane1 = test1.calki,
            # opis1 = "Metoda trapezow",
            dane1 = test2.calki,
            opis1 = "Metoda parabol",
            dane2 = test3.calki,
            opis2 = "Metoda 3/8 Newtona"
        )
"""Przyklad zastosowania metod przyblizonych"""

import wielomian, wykresy
import bisekcja, sieczne, styczne

class Przyklad1:
  
    def __init__(self, typ):
        """Konstruktor klasy"""
        # dobor przedzialu
        if typ == 1:
            # tworzymy wielomian 7x^3 + 3x^2 - 6x + 3
            self.wsp = [3.0, -6.0, 3.0, 7.0]
            # okreslamy krance przedzialu
            self.a = -5.0
            self.b = 5.0
        # zmniejszamy przedzial
        elif typ == 2:
            self.wsp = [3.0, -6.0, 3.0, 7.0]
            self.a = -2.0
            self.b = -1.0
        # wiecej niz jedno rozwiazanie, niespelnione 2 i 3 warunek
        elif typ == 3:
            self.wsp = [0.0, 1.0, 0.0, -1.0]
            self.a = -1.99
            self.b = 2.1
        # zaden z WZ niespelniony
        elif typ == 4:
            self.wsp = [2.0, -1.0, 0.0, 1.0]
            self.a = -0.5
            self.b = 2.0
        self.f = wielomian.Wielomian(self.wsp)
        # okreslamy parametry eksperymentu
        self.n = 40
        self.epsilon = 1.0e-7
    
    def porownaj(self, war_stopu):
        """Metoda porownujaca metody przyblizone,
            parametr war_stopu okresla kryterium stopu:
            0 - zadana liczba iteracji
            1 - iteracje zatrzymywane, gdy dwa kolejne przyblizenia
                dostatecznie blisko siebie"""
        # metoda bisekcji
        print("Metoda bisekcji")
        test1 = bisekcja.Bisekcja(
            wiel = self.f,
            lewy_kp = self.a,
            prawy_kp = self.b)
        if (war_stopu == 0):
            ans1 = test1.iteruj(iteracje = self.n, wyswietlaj = 1)
        else:
            ans1 = test1.iteruj_roznica(eps = self.epsilon, wyswietlaj = 1)
        if ans1 > 0:
            test1.sprawdz_rozwiazanie()
        # metoda siecznych
        print("-"*30)
        print("Metoda siecznych")
        test2 = sieczne.Sieczne(
            wiel = self.f,
            lewy_kp = self.a,
            prawy_kp = self.b)
        if (war_stopu == 0):
            ans2 = test2.iteruj(iteracje = self.n, wyswietlaj = 1)
        else:
            ans2 = test2.iteruj_roznica(eps = self.epsilon, wyswietlaj = 1)
        if ans2 > 0:
            test2.sprawdz_rozwiazanie()
        # metoda stycznych
        print("-"*30)
        print("Metoda stycznych")
        test3 = styczne.Styczne(
            wiel = self.f,
            lewy_kp = self.a,
            prawy_kp = self.b)
        if (war_stopu == 0):
            ans3 = test3.iteruj(iteracje = self.n, wyswietlaj = 1)
        else:
            ans3 = test3.iteruj_roznica(eps = self.epsilon, wyswietlaj = 1)
        if ans3 > 0:
            test3.sprawdz_rozwiazanie()
        # obrazujemy zbieznosc tych metod na wykresie
        wykres = wykresy.Wykresy()
        # sprawdzamy, czy metody siecznych i stycznych zostaly zastosowane
        if ans2 == 0:
            test2.x = []
        if ans3 == 0:
            test3.x = []
        wykres.badaj_zbieznosc(
            tytul = "Metody przyblizone",
            opis_OY = "Przyblizenia rozwiazania",
            dane1 = test1.x,
            opis1 = "Metoda bisekcji",
            dane2 = test2.x,
            opis2 = "Metoda siecznych",
            dane3 = test3.x,
            opis3 = "Metoda stycznych"
        )
        
    def warunki_zbieznosci(self):
        """Metoda obrazujaca warunki zbieznosci"""
        wykres1 = wykresy.Wykresy()
        wykres1.wykres_wielomianow(
            f = self.f,
            a = self.a,
            b = self.b,
            opis = "Warunki zbieznosci")        
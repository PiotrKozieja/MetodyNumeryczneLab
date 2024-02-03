"""Porownanie metod przyblizonych"""

import wielomian, wykresy
import bisekcja, sieczne, styczne

class Zadanie1:
  
    def __init__(self):
        """Konstruktor klasy"""
        # dobor przedzialu
        # tworzymy wielomian wspisujac wspolczynniki a0, a1, a2, a3
        self.wsp = [1.0, 5.0, 2.0, 4.0]
        self.f = wielomian.Wielomian(self.wsp)
        # okreslamy krance przedzialu
        self.a = -0.35
        self.b = -0.19
        # okreslamy parametry eksperymentu
        self.n = 40
        self.epsilon = 1.0e-15
    
    def porownaj(self, war_stopu):
        """Metoda porownujaca metody przyblizone,
            parametr war_stopu okresla kryterium stopu:
            0 - zadana liczba iteracji
            1 - iteracje zatrzymywane, gdy dwa kolejne przyblizenia
                dostatecznie blisko siebie"""
        # metoda bisekcji
        # print("Metoda bisekcji")
        # test1 = bisekcja.Bisekcja(
        #     wiel = self.f,
        #     lewy_kp = self.a,
        #     prawy_kp = self.b)
        # if (war_stopu == 0):
        #     ans1 = test1.iteruj(iteracje = self.n, wyswietlaj = 1)
        # else:
        #     ans1 = test1.iteruj_roznica(eps = self.epsilon, wyswietlaj = 1)
        # if ans1 > 0:
        #     test1.sprawdz_rozwiazanie()
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
            # dane1 = test1.x,
            # opis1 = "Metoda bisekcji",
            dane1 = test2.x,
            opis1 = "Metoda siecznych",
            dane2 = test3.x,
            opis2 = "Metoda stycznych"
        )
        
    def warunki_zbieznosci(self):
        """Metoda obrazujaca warunki zbieznosci"""
        wykres1 = wykresy.Wykresy()
        wykres1.wykres_wielomianow(
            f = self.f,
            a = self.a,
            b = self.b,
            opis = "Warunki zbieznosci")        
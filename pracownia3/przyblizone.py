"""Przyklad zastosowania metod przyblizonych"""

import wielomian, wykresy
import bisekcja, sieczne, styczne

def testy(typ):
    # okreslamy wspolczynniki wielomianu: a0, a1, a2, ...
    wsp = [-2.0, 0.0, 0.0, 1.0]
    # tworzymy wielomian
    f = wielomian.Wielomian(wsp)
    # okreslamy krance przedzialu oraz liczbe iteracji
    a = 1.0
    b = 2.0
    n = 30
    epsilon = 1e-10
    # iterujemy metody przyblizone zadana liczbe iteracji
    if typ == 1:    
        # metoda bisekcji
        test1 = bisekcja.Bisekcja(wiel = f, lewy_kp = a, prawy_kp = b)
        test1.iteruj(iteracje = n, wyswietlaj = 1)
        test1.sprawdz_rozwiazanie()
        # metoda siecznych
        test2 = sieczne.Sieczne(wiel = f, lewy_kp = a, prawy_kp = b)
        test2.iteruj(iteracje = n, wyswietlaj = 1)
        test2.sprawdz_rozwiazanie()
        # metoda stycznych
        test3 = styczne.Styczne(wiel = f, lewy_kp = a, prawy_kp = b)
        test3.iteruj(iteracje = n, wyswietlaj = 1)
        test3.sprawdz_rozwiazanie()
        # obrazujemy zbieznosc tych metod na wykresie
        wykres1 = wykresy.Wykresy()
        wykres1.badaj_zbieznosc(
            tytul = "Metody przyblizone",
            opis_OY = "Przyblizenia rozwiazania",
            dane1 = test1.x,
            opis1 = "Metoda bisekcji",
            dane2 = test2.x,
            opis2 = "Metoda siecznych",
            dane3 = test3.x,
            opis3 = "Metoda stycznych"
        )
    # iterujemy do momentu, gdy kolejne przyblizenia roznia sie o mniej niz eps
    if typ == 2:    
        # metoda bisekcji
        test1 = bisekcja.Bisekcja(wiel = f, lewy_kp = a, prawy_kp = b)
        test1.iteruj_roznica(eps = epsilon, wyswietlaj = 1)
        test1.sprawdz_rozwiazanie()
        # metoda siecznych
        test2 = sieczne.Sieczne(wiel = f, lewy_kp = a, prawy_kp = b)
        test2.iteruj_roznica(eps = epsilon, wyswietlaj = 1)
        test2.sprawdz_rozwiazanie()
        # metoda stycznych
        test3 = styczne.Styczne(wiel = f, lewy_kp = a, prawy_kp = b)
        test3.iteruj_roznica(eps = epsilon, wyswietlaj = 1)
        test3.sprawdz_rozwiazanie()
        # obrazujemy zbieznosc tych metod na wykresie
        wykres2 = wykresy.Wykresy()
        wykres2.badaj_zbieznosc(
            tytul = "Metody przyblizone",
            opis_OY = "Przyblizenia rozwiazania",
            dane1 = test1.x,
            opis1 = "Metoda bisekcji",
            dane2 = test2.x,
            opis2 = "Metoda siecznych",
            dane3 = test3.x,
            opis3 = "Metoda stycznych"
        )
        
if __name__ == '__main__':
    testy(1)
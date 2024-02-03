"""Przyklad zastosowania metod calkowania"""

import funkcja, wykresy
import metodatrapezow, metodaparabol, metodanewtona

def testy(typ):
    # okreslamy funkcje
    f = funkcja.Funkcja()
    # okreslamy krance przedzialu oraz liczbe iteracji, parametr eps
    a = 1.0
    b = 2.0
    n = 30
    epsilon = 1e-6
    # obliczamy przyblizenia dla zadanej maksymalnej liczby podprzedzialow
    if typ == 1:    
        # metoda trapezow
        print("Metoda trapezow")
        test1 = metodatrapezow.MetodaTrapezow(
            funkcja = f,
            lewy_kp = a,
            prawy_kp = b)
        test1.iteruj(iteracje = n, wyswietlaj = 1)
        # metoda parabol
        print("\nMetoda parabol")
        test2 = metodaparabol.MetodaParabol(
            funkcja = f,
            lewy_kp = a,
            prawy_kp = b)
        test2.iteruj(iteracje = n, wyswietlaj = 1)
        # metoda 3/8 Newtona
        print("\nMetoda 3/8 Newtona")
        test3 = metodanewtona.MetodaNewtona(
            funkcja = f,
            lewy_kp = a,
            prawy_kp = b)
        test3.iteruj(iteracje = n, wyswietlaj = 1)
        # obrazujemy zbieznosc tych metod na wykresie
        wykres1 = wykresy.Wykresy()
        wykres1.badaj_zbieznosc(
            tytul = "Metody calkowania",
            opis_OY = "Przyblizenia calki",
            dane1 = test1.calki,
            opis1 = "Metoda trapezow",
            dane2 = test2.calki,
            opis2 = "Metoda parabol",
            dane3 = test3.calki,
            opis3 = "Metoda 3/8 Newtona"
        )
    # zwiekszamy liczbe podprzedzialow jak dlugo roznica kolejnych
    # przyblizen nie przekracza eps
    if typ == 2:    
        # metoda trapezow
        print("Metoda trapezow")
        test1 = metodatrapezow.MetodaTrapezow(
            funkcja = f,
            lewy_kp = a,
            prawy_kp = b)
        test1.iteruj_roznica(eps = epsilon, wyswietlaj = 1)
        # metoda parabol
        print("\nMetoda parabol")
        test2 = metodaparabol.MetodaParabol(
            funkcja = f,
            lewy_kp = a,
            prawy_kp = b)
        test2.iteruj_roznica(eps = epsilon, wyswietlaj = 1)
        # metoda 3/8 Newtona
        print("\nMetoda 3/8 Newtona")
        test3 = metodanewtona.MetodaNewtona(
            funkcja = f,
            lewy_kp = a,
            prawy_kp = b)
        test3.iteruj_roznica(eps = epsilon, wyswietlaj = 1)
        # obrazujemy zbieznosc tych metod na wykresie
        wykres2 = wykresy.Wykresy()
        wykres2.badaj_zbieznosc(
            tytul = "Metody calkowania",
            opis_OY = "Przyblizenia calki",
            dane1 = test1.calki,
            opis1 = "Metoda trapezow",
            dane2 = test2.calki,
            opis2 = "Metoda parabol",
            dane3 = test3.calki,
            opis3 = "Metoda 3/8 Newtona"
        )
        
if __name__ == '__main__':
    testy(1)
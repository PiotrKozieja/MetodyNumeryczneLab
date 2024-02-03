"""Klasa realizjujaca metode siecznych"""

from typing import List

class Sieczne:
  
    def __init__(self, wiel, lewy_kp, prawy_kp):
        """Konstruktor okreslajacy problem"""
        self.funkcja = wiel                    # funkcja f(x)
        # obliczamy pochodne
        self.pochodna1 = self.funkcja.pochodna()
        self.pochodna2 = self.pochodna1.pochodna()
        self.a = lewy_kp                       # lewy kraniec przedzialu
        self.b = prawy_kp                      # prawy kraniec przedzialu
        self.x : List = []                     # lista przyblizen
        self.kmax = 10000                      # maskymalna liczba iteracji
    
    def iteruj(self, iteracje, wyswietlaj = 0):
        """Metoda wykonujaca zadana liczbe iteracji;
            dodatkowy parametr wyswietlaj pozwala wyswietlac
            kolejne przyblizenia; funkcja zwraca ostatnie przyblizenie
            lub 0, jeżeli metoda nie moze byc zastosowana"""
        # resetuje liste
        self.x = []
        # ustalam punkt nieruchomy - obliczam wartosci 2. pochodnej
        wart_poch2_a = self.pochodna2.wartosc(self.a)
        wart_poch2_b = self.pochodna2.wartosc(self.b)
        # obliczam wartosci na krancach aktualnego przedzialu
        wart_a = self.funkcja.wartosc(self.a)
        wart_b = self.funkcja.wartosc(self.b)
        # sprawdzam, ktory z punktow powinien byc nieruchomy (nazywam go c)
        # punkt startowy - oznaczam x_akt
        if wart_a * wart_poch2_a > 0:
            c = self.a
            wart_c = wart_a
            x_akt = self.b
        elif wart_b * wart_poch2_b > 0:
            c = self.b
            wart_c = wart_b
            x_akt = self.a
        else:
            print("Nie mozna zastosowac metody.")
            return 0
        # dodaje przyblizenie startowe do listy
        self.x.append(x_akt)
        # wyswietlam przyblizenie startowe
        if wyswietlaj == 1:
            print(f"0. \t {x_akt}")
        for k in range(iteracje):
            # obliczam wartosc w punkcie x_akt
            wart_x = self.funkcja.wartosc(x_akt)
            x_akt -= wart_x * (x_akt-c) / (wart_x-wart_c) 
            self.x.append(x_akt)
            if wyswietlaj == 1:
                print(f"{k+1}. \t {x_akt}")
        return x_akt
    
    def iteruj_roznica(self, eps, wyswietlaj = 0):
        """Metoda wykonujaca iteracje do momentu, gdy roznica kolejnych
            przyblizen nie przekracza eps; dodatkowy parametr
            wyswietlaj pozwala wyswietlac kolejne przyblizenia;
            funkcja zwraca liczbe iteracji"""
        # resetuje liste
        self.x = []
        # ustalam punkt nieruchomy - obliczam wartosci 2. pochodnej
        wart_poch2_a = self.pochodna2.wartosc(self.a)
        wart_poch2_b = self.pochodna2.wartosc(self.b)
        # obliczam wartosci na krancach aktualnego przedzialu
        wart_a = self.funkcja.wartosc(self.a)
        wart_b = self.funkcja.wartosc(self.b)
        # sprawdzam, ktory z punktow powinien byc nieruchomy (nazywam go c)
        # punkt startowy - oznaczam x_akt
        if wart_a * wart_poch2_a > 0:
            c = self.a
            wart_c = wart_a
            x_akt = self.b
        elif wart_b * wart_poch2_b > 0:
            c = self.b
            wart_c = wart_b
            x_akt = self.a
        else:
            print("Nie mozna zastosowac metody.")
            return 0
        # dodaje przyblizenie startowe do listy
        self.x.append(x_akt)
        k = 0
        # wyswietlam przyblizenie startowe
        if wyswietlaj == 1:
            print(f"{k}. \t {x_akt}")
        roznica = 100.0
        while roznica > eps:
            k += 1
            # obliczam wartosc w punkcie x_akt
            wart_x = self.funkcja.wartosc(x_akt)
            x_akt -= wart_x * (x_akt-c) / (wart_x-wart_c) 
            self.x.append(x_akt)
            if wyswietlaj == 1:
                print(f"{k}. \t {x_akt}")
            roznica = abs(self.x[-1] - self.x[-2])
            # jezeli przkroczono maksymalna liczbe rozwiazan - przerywam
            if k == self.kmax:
                print("Przekroczono maksymalna liczbe iteraji.")
                break
        return k
    
    def sprawdz_rozwiazanie(self):
        """Metoda sprwadzajaca niedokladnosc rozwiazania"""
        niedokl = abs(self.funkcja.wartosc(self.x[-1]))
        print(f"Niedokladnosc rozwiazania: {niedokl}")
        return niedokl
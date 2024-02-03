"""Klasa realizjujaca metode bisekcji"""

from typing import List

class Bisekcja:
  
    def __init__(self, wiel, lewy_kp, prawy_kp):
        """Konstruktor okreslajacy problem"""
        self.funkcja = wiel                    # funkcja f(x)
        self.a = lewy_kp                       # lewy kraniec przedzialu
        self.b = prawy_kp                      # prawy kraniec przedzialu
        self.x : List = []                     # lista przyblizen
        self.kmax = 10000                      # maskymalna liczba iteracji
    
    def iteruj(self, iteracje, wyswietlaj = 0):
        """Metoda wykonujaca zadana liczbe iteracji;
            dodatkowy parametr wyswietlaj pozwala wyswietlac
            kolejne przyblizenia; funkcja zwraca ostatnie przyblizenie"""
        lewy_kp = self.a            # lewy kraniec aktualnego przedzialu
        prawy_kp = self.b           # prawy kraniec aktualnego przedzialu
        # resetuje liste
        self.x = []
        # obliczam wartosci na krancach aktualnego przedzialu
        wart_lewy = self.funkcja.wartosc(lewy_kp)
        wart_prawy = self.funkcja.wartosc(prawy_kp)
        srodek = (lewy_kp+prawy_kp) / 2.0
        # dodaje przyblizenie startowe do listy
        self.x.append(srodek)
        # wyswietlam przyblizenie startowe
        if wyswietlaj == 1:
            print(f"0. \t {srodek}")
        for k in range(iteracje):
            # obliczam wartosc
            wart_srodek = self.funkcja.wartosc(srodek)
            if wart_lewy * wart_srodek > 0:
                lewy_kp = srodek
                wart_lewy = wart_srodek
                srodek = (srodek+prawy_kp) / 2.0
                self.x.append(srodek)
            elif wart_prawy * wart_srodek > 0:
                prawy_kp = srodek
                wart_prawy = wart_srodek
                srodek = (srodek + lewy_kp) / 2.0
                self.x.append(srodek)
            else:
                # jezeli rozwiazanie jest w srodku przdzialu - przerywam
                break
            if wyswietlaj == 1:
                print(f"{k+1}. \t {srodek}")
        return srodek
    
    def iteruj_roznica(self, eps, wyswietlaj = 0):
        """Metoda wykonujaca iteracje do momentu, gdy roznica kolejnych
            przyblizen nie przekracza eps; dodatkowy parametr
            wyswietlaj pozwala wyswietlac kolejne przyblizenia;
            funkcja zwraca liczbe iteracji"""
        lewy_kp = self.a            # lewy kraniec aktualnego przedzialu
        prawy_kp = self.b           # prawy kraniec aktualnego przedzialu
        # resetuje liste
        self.x = []
        # obliczam wartosci na krancach aktualnego przedzialu
        wart_lewy = self.funkcja.wartosc(lewy_kp)
        wart_prawy = self.funkcja.wartosc(prawy_kp)
        srodek = (lewy_kp+prawy_kp) / 2.0
        # dodaje przyblizenie startowe do listy
        self.x.append(srodek)
        k = 0
        # wyswietlam przyblizenie startowe
        if wyswietlaj == 1:
            print(f"{k}. \t {srodek}")
        roznica = 100.0
        while roznica > eps:
            k += 1
            # obliczam wartosc
            wart_srodek = self.funkcja.wartosc(srodek)
            if wart_lewy * wart_srodek > 0:
                lewy_kp = srodek
                wart_lewy = wart_srodek
                srodek = (srodek+prawy_kp) / 2.0
                self.x.append(srodek)
            elif wart_prawy * wart_srodek > 0:
                prawy_kp = srodek
                wart_prawy = wart_srodek
                srodek = (srodek + lewy_kp) / 2.0
                self.x.append(srodek)
            else:
                # jezeli rozwiazanie jest w srodku przdzialu - przerywam
                break
            if wyswietlaj == 1:
                print(f"{k}. \t {srodek}")
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
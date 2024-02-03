"""Klasa realizjujaca metode 3/8 Newtona"""

from typing import List

class MetodaNewtona:
  
    def __init__(self, funkcja, lewy_kp, prawy_kp):
        """Konstruktor okreslajacy problem"""
        self.f = funkcja                       # funkcja podcalkowa
        self.a = lewy_kp                       # lewy kraniec przedzialu
        self.b = prawy_kp                      # prawy kraniec przedzialu
        self.calki : List = []                 # lista przyblizen
        self.kmax = 10000                      # maskymalna liczba iteracji
    
    def calkuj(self, n):
        """Metoda obliczajaca przyblizenie calki
            dla zadanej liczby podprzedzialow - n"""
        h = (self.b-self.a) / (3.0*n)
        calka = self.f.wartosc(self.a) + self.f.wartosc(self.b)
        calka += 3*self.f.wartosc(self.a+h)
        calka += 3*self.f.wartosc(self.a+2*h)
        for i in range(1, n):
            calka += 2*self.f.wartosc(self.a+3*i*h)
            calka += 3*self.f.wartosc(self.a+(3*i+1)*h)
            calka += 3*self.f.wartosc(self.a+(3*i+2)*h)
        return 3*h*calka/8
        
    def iteruj(self, iteracje, wyswietlaj = 0):
        """Metoda wykonujaca zadana liczbe iteracji;
            dodatkowy parametr wyswietlaj pozwala wyswietlac
            kolejne przyblizenia; funkcja zwraca ostatnie przyblizenie"""
        # resetuje liste
        self.calki = []
        for k in range(iteracje):
            # obliczam wartosc w punkcie x_akt
            calka = self.calkuj(k+1)
            self.calki.append(calka)
            if wyswietlaj == 1:
                print(f"{k+1}. \t {calka}")
        return calka
    
    def iteruj_roznica(self, eps, wyswietlaj = 0):
        """Metoda wykonujaca iteracje do momentu, gdy roznica kolejnych
            przyblizen nie przekracza eps; dodatkowy parametr
            wyswietlaj pozwala wyswietlac kolejne przyblizenia;
            funkcja zwraca liczbe iteracji"""
        # resetuje liste
        self.calki = []
        k = 0
        calka = self.calkuj(k+1)
        self.calki.append(calka)
        if wyswietlaj == 1:
            print(f"{k+1}. \t {calka}")
        roznica = 1000.0
        while roznica > eps:
            k += 1
            calka = self.calkuj(k+1)
            self.calki.append(calka)
            if wyswietlaj == 1:
                print(f"{k+1}. \t {calka}")
            roznica = abs(self.calki[-1] - self.calki[-2])
            # jezeli przkroczono maksymalna liczbe rozwiazan - przerywam
            if k == self.kmax:
                print("Przekroczono maksymalna liczbe iteraji.")
                break
        return k
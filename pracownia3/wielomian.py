"""Klasa przechowujaca wielomian"""

from typing import List

class Wielomian:
  
    def __init__(self, wspolczynniki):
        """Konstruktor wielomianow
            tablica wspolczynnikow jest podawana poczawczy od wyrazu wolnego
            tj. a[i] jest wspolczynnikiem stojacym przy x^i"""
        self.n = len(wspolczynniki)       # stopien wielomianu
        self.a = wspolczynniki.copy()        # tablica wspolczynnikow
        
    def wartosc(self, x):
        """Metoda obliczajaca wartosc wielomianu w punkcie x"""
        wart = self.a[0]
        for i in range(1, self.n):
            wart += self.a[i]*pow(x, i)
        return wart
    
    def pochodna(self):
        """Metoda obliczajaca pochodna wielomianu"""
        wsp : List = []
        for i in range(self.n-1):
            wsp.append(self.a[i+1] * (i+1))
        poch = Wielomian(wsp)
        return poch
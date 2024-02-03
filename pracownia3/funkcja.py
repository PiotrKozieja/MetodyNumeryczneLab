"""Klasa przechowujaca funkcje"""

import math

class Funkcja:
  
    def __init__(self):
        """Konstruktor klasy Funkcja"""
        pass
    
    def wartosc(self, x):
        """Metoda obliczajaca wartosc funkcji w punkcie x"""
        wart = 4*math.sin(49*x+2)+math.sqrt(1+x*x)
        return wart
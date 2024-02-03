"""Klasa, w ktorej mozna zrealizowac rozwiazanie Zadania 1"""

import uklad, wykresy
import iteracjaprosta, iteracjaseidela
import numpy as np

class Zadanie1:

    def __init__(self):
        """Konstruktor"""
        self.eps = 1e-10
        self.alfa = 0.3
        self.n = 100
        self.k = 30            # liczba pomiarow dla jednej wartosci parametru
        self.norma = 1
        
        
    def testy(self):
        """Testy wstepne"""
        # miejsce na rozwiazanie pierwszej czesci zadania 1
        ukl1 = uklad.Uklad(wymiar=10)
        ukl2 = uklad.Uklad(wymiar=120)

        ukl1.losuj_uklad_symetryczny_dodatnio_okreslony()
        ukl2.losuj_uklad_symetryczny_dodatnio_okreslony()

        test1 = iteracjaseidela.IteracjaSeidela(ukl1)
        test2 = iteracjaseidela.IteracjaSeidela(ukl2)

        ukl1.wypisz_normy_macierzy()

        test1.przygotuj()
        test2.przygotuj()

        # iteracja prosta przy mniejszym n
        test1.iteruj(
            iteracje = self.k,
            norma = self.norma
            )
        seria1 = test1.normy.copy()
        niedokl1 = test1.sprawdz_rozwiazanie(self.norma)

        print(f"Niedokladnosc rozwiazania: {niedokl1}")

        # iteracja prosta przy wiekszym n
        test2.iteruj(
            iteracje=self.k,
            norma=self.norma)
        seria2 = test2.normy.copy()
        #test2.wypisz_normy()
        niedokl2 = test2.sprawdz_rozwiazanie(self.norma)

        print(f"Niedokladnosc rozwiazania: {niedokl2}")

        print('norma 1')
        test1.zwroc_norme()
 
        print('norma 2')
        test2.zwroc_norme()

        wykres_test = wykresy.Wykresy()
        wykres_test.badaj_zbieznosc(
            tytul="Zbieznosc metod iteracyjnych",
            opis_OY="Normy przyblizeń",
            dane1=seria1,
            opis1="Iteracja Seidla przy mniejszym n",
            dane2=seria2,
            opis2="Iteracja Seidla przy wiekszym n"
        )
        
    def badaj_zbieznosc(self):
        """Badam zbieznosc metody iteracji prostej"""
        param = [10,20,30,40,50,60,70,80,90,100,110,120]
        sr_norma_macierzy = []
        sr_niedokladnosc = []
        for n in param :
            u1 = uklad.Uklad(wymiar=n)
            norma_macierzy = 0.0
            niedokladnosc = 0.0
            iteracje = 0
            while iteracje < self.k:
                u1.losuj_uklad_symetryczny_dodatnio_okreslony()
                test1 = iteracjaseidela.IteracjaSeidela(ukl=u1)
                test1.przygotuj()
                norma_D = u1.norma_macierzy(
                    typ=self.norma,
                    macierz=test1.D
                )
                test1.iteruj(
                    iteracje = self.k,
                    norma = self.norma
                )
                niedokl = test1.sprawdz_rozwiazanie(norma=self.norma)
            
                norma_macierzy += norma_D
                niedokladnosc += niedokl
                iteracje += 1
            sr_norma_macierzy.append(norma_macierzy / self.k)
            sr_niedokladnosc.append(niedokladnosc / self.k)
        print("Wielkosc \nmacierzy \t \t ||D|| \t   Niedokladnosc")
        print("------" * 9)
        for i in range(len(param)):
            wyniki = f"{param[i]} \t\t\t"
            wyniki += f"{sr_norma_macierzy[i]:.6f} \t\t"
            wyniki += f"{sr_niedokladnosc[i]:.6e} \n"
            print(wyniki)
        return 0
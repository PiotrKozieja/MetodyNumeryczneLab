"""Przyklady:
    1 - porownania metod przyblizonych do znalezienia miejsca zerowego
        pewnego wielomianu
    2 - porownanie metod przyblizonych calkowania skomplikowanej funkcji"""

import przyklad1, przyklad2, zadanie1, zadanie2

def testy(typ):
    if typ == 1:    
        # porownanie metod bisekcji, stycznych i siecznych
        # poczatkowo wybieramy duzy przedzial
        test1 = przyklad1.Przyklad1(typ = 1)
        test1.warunki_zbieznosci()
        test1.porownaj(war_stopu = 0)
    if typ == 2:    
        # przyklad calki ze skomplikowanej funkcji
        test2 = przyklad2.Przyklad2()
        test2.porownaj(war_stopu = 1)
    if typ == 3:    
        # sekcja na realizacje zadania 1
        zad1 = zadanie1.Zadanie1()
        zad1.warunki_zbieznosci()
        zad1.porownaj(war_stopu = 1 )
    if typ == 4:    
        # sekcja na realizacje zadania 2
        zad2 = zadanie2.Zadanie2()
        zad2.porownaj(war_stopu = 1)
        
if __name__ == '__main__':
    testy(4)
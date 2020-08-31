#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

#--------------------------------------------------------------------------------------------
from itertools import permutations

#očitno je, da se dolžina števila ne smo spremeniti

def st_stevk(n):
    sez = []
    while n > 9:
        sez.append(n % 10)
        n = n // 10
    sez.append(n)
    return len(sez)

def mnozica_stevk(n):
    mnozica = set()
    while n > 9:
        mnozica.add(n % 10)
        n = n // 10
    mnozica.add(n)
    return mnozica

sez = []
n = 26#do tam vidimo da ni rezultata, naprej se nam ne da gledat
while len(sez) < 1:
    if st_stevk(n) == st_stevk(2 * n) == st_stevk(3 * n) == st_stevk(4 * n) == st_stevk(5 * n) == st_stevk(6 * n):
        if mnozica_stevk(n) == mnozica_stevk(2 * n) == mnozica_stevk(3 * n) == mnozica_stevk(4 * n)  == mnozica_stevk(5 * n)  == mnozica_stevk(6 * n):
            print(n)
            sez.append(n)
    n += 1
    






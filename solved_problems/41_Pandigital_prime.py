#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

#----------------------------------------------------------
from itertools import permutations

def is_prime(n):

    sez = []

    for i in range(1, int(n + 1)):

        if n % i == 0:

            sez += [i]

    return len(sez) == 2

#9,8-digit:vsota števk je deljiva z 9, torej ne bo nobeno število praštevilo

#7:na zadnjem mestu ne smemo imeti:2,4,5,6 

seznam = []

#na zadnjem mestu 1(najprej poskusimo z 1, nato s 3 in 7 in vzamemo max, če še vedno ne najdemo gremo na n = 6):
perm7_1 = permutations([2, 3, 4, 5, 6, 7])
sez7_1 = []

for i in list(perm7_1)[::-1]:#obrnemo, da je največje št na začetku
    a = ""
    for st in i:
        a += str(st)
    a += str(1)
    sez7_1.append(int(a))
for st in sez7_1:
    if is_prime(st):
        seznam.append(st)
        print(seznam)
        break
 
#na zadnjem mestu 3:
perm7_3 = permutations([1, 2, 4, 5, 6, 7])
sez7_3 = []

for i in list(perm7_3)[::-1]:#obrnemo, da je največje št na začetku
    a = ""
    for st in i:
        a += str(st)
    a += str(3)
    sez7_3.append(int(a))
for st in sez7_3:
    if is_prime(st):
        seznam.append(st)
        print(seznam)
        break

#na zadnjem mestu 5:
perm7_5 = permutations([1, 2, 3, 4, 6, 7])
sez7_5 = []

for i in list(perm7_5)[::-1]:#obrnemo, da je največje št na začetku
    a = ""
    for st in i:
        a += str(st)
    a += str(5)
    sez7_5.append(int(a))
for st in sez7_5:
    if is_prime(st):
        seznam.append(st)
        print(seznam)
        break

print(max(seznam))

#za tretji seznam potrebujemo precejčasa, toda medtem opazimo, da ima drugo št na prvih treh mestih števke 765
#[7625341, 7652413](max od prvega in drugega seznama)
#ker ima tretje št. na zadnjem mestu 5, bo gotovo manjše od prvih dveh --> največje št je 7652413
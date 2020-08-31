#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

#-------------------------------------------------------------
from itertools import permutations

perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sez_perm = []

for i in list(perm):
    a = ""
    for st in i:
        a += str(st)
    sez_perm.append(int(a))

#pri permutacijah ničlo na prvem mestu izpusti
#dolžina n je vedno 10 razen v primeru ko je ničla na prvem mestu

def d2d3d4(n):
    if "0" in str(n):#ničla je znotraj, dolžina je 10
        n = int(str(n)[1:4])
        return n % 2 == 0
    else:
        n = int(str(n)[0:3])
        return n % 2 == 0

def d3d4d5(n):
    if "0" in str(n):#ničla je znotraj, dolžina je 10
        n = int(str(n)[2:5])
        return n % 3 == 0
    else:
        n = int(str(n)[1:4])
        return n % 3 == 0

def d4d5d6(n):
    if "0" in str(n):#ničla je znotraj, dolžina je 10
        n = int(str(n)[3:6])
        return n % 5 == 0
    else:
        n = int(str(n)[2:5])
        return n % 5 == 0

def d5d6d7(n):
    if "0" in str(n):#ničla je znotraj, dolžina je 10
        n = int(str(n)[4:7])
        return n % 7 == 0
    else:
        n = int(str(n)[3:6])
        return n % 7 == 0

def d6d7d8(n):
    if "0" in str(n):#ničla je znotraj, dolžina je 10
        n = int(str(n)[5:8])
        return n % 11 == 0
    else:
        n = int(str(n)[4:7])
        return n % 11 == 0

def d7d8d9(n):
    if "0" in str(n):#ničla je znotraj, dolžina je 10
        n = int(str(n)[6:9])
        return n % 13 == 0
    else:
        n = int(str(n)[5:8])
        return n % 13 == 0

def d8d9d10(n):
    if "0" in str(n):#ničla je znotraj, dolžina je 10
        n = int(str(n)[7:10])
        return n % 17 == 0
    else:
        n = int(str(n)[6:9])
        return n % 17 == 0

seznam = []
for i in sez_perm:
    if d2d3d4(i) and d3d4d5(i) and d4d5d6(i) and d5d6d7(i) and d6d7d8(i) and d7d8d9(i) and d8d9d10(i):
        seznam.append(i)
print(sum(seznam))

#za 2, 3 in 5 bi namesto te funkcije lahko uporabili ravila za deljenje: primerjali zadnjo števko za 2 in 5 in vsoto za 3
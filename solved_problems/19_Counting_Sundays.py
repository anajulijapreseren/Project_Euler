#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

sez1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sez2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#v dvajsetem stoletju imamo prestopno leto vsaka 4 leta, saj je 2000 deljivo s 400

#ugotovimo kateri dan je 1.1.1901
a = 1
for st in sez1:
    a += st
print(a % 7)
 # dobimo rezultat 2, kar je torek

#funkcija je narejena za 20.tisočletje, za druga leta pa jo je potrebno izboljšati
def prvi_dnevi(leto):
    """funkcija bo vrnila seznam z indeksi prvih dnevov v mesecu(vsak dan dodamo 1),
    začela pa bo šteti 1.1.leto in končala 31.12.(leto + 99)"""
    sez = []
    a = 2
    for i in range(leto, leto + 100):
        if i % 4 == 0:#prestopno leto
            for st in sez2:
                a += st
                sez.append(a)
        else:
            for st in sez1:
                a += st
                sez.append(a)
    return sez[:-1]#zadnjega zbrisemo ker pride na naslednje leto

def nedelje(seznam):
    st = 0
    for i in seznam:
        if i % 7 == 0:#nedeljam pripada ravno indeks 7
            st += 1
    return st

print(nedelje(prvi_dnevi(1901)))

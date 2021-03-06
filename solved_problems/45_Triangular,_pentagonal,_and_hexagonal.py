#Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
#Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
#It can be verified that T285 = P165 = H143 = 40755.
#
#Find the next triangle number that is also pentagonal and hexagonal.

#----------------------------------------------------------------------------------

#vidimo, da so števila triangle najmanjša-smiselno je pogledati, če se element s tega seznama nahaja v drugih dveh
#če se v tem koraku ne nahaja se ne bo tudi v naslednjem, saj se števila večajo in lahko na ta element pozabimo

sez = []
tria = []
penta = []
hexa = []
t = 268
p = 166
h = 144
while len(sez) < 1:
    tria.append(t * (t + 1) / 2)
    penta.append(p * ((3 * p) - 1) / 2)
    hexa.append(h * (2 * h - 1))
    if (t * (t + 1) / 2) in penta:
        if (t * (t + 1) / 2) in hexa:
            sez.append((t * (t + 1) / 2))
    t += 1
    p += 1
    h += 1
print(sez)

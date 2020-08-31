#A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

def sestej_stevke(n):
    """dobimo seznam, ki vsebuje posamezne cifre števila, potem pa ta seznam seštejemo"""
    sez = []
    while n > 9:
        ostanek = n % 10
        n = n // 10
        sez.append(ostanek)
    sez.append(n)
    return sum(sez)

maksimum = 0
for a in range(2, 100):
    for b in range(1, 100):
        maksimum = max(maksimum, sestej_stevke(a ** b))
print(maksimum)
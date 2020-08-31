def je_palindrom(st):
    return str(st) == str(st)[::-1]

def min_produkt(n):
    """vrednost produkta najmanjsih n-mestnih st"""
    return 10**(2*n-2) 

def max_produkt(n):
    """vrednost produkta najvecjih n-mestnih st"""
    return (10**(n) - 1) * (10**(n) - 1)

def max_palindrom(n):
    """max palindrom, ki je produkt n-mestnih stevil"""
    zgoraj = 10 ** n - 1
    spodaj = 10 ** (n-1)
    a = zgoraj
    b = zgoraj
    sez = []
    while a>spodaj:
        while b >= spodaj:
            st = a*b
            if je_palindrom(st):
                sez.append([st])
            b = b-1
        a = a-1
        zgoraj = zgoraj - 1
        b = zgoraj
        sez.sort()
    return sez[-1]
            
print(max_palindrom(3))

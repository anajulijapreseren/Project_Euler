# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2**1000?

print(2**1000)

def naredi_seznam(n):
    """dobimo seznam, ki vsebuje posamezne cifre števila"""
    sez = []
    while n > 9:
        ostanek = n % 10
        n = n // 10
        sez.append(ostanek)
    sez.append(n)
    return sez[::-1]

print(sum(naredi_seznam(2**1000)))
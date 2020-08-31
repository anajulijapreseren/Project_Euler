#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!

def factorial(n):
    st = 1
    for i in range(1, n+1):
        st *= i
    return st

def naredi_seznam(n):
    """dobimo seznam, ki vsebuje posamezne cifre števila"""
    sez = []
    while n > 9:
        ostanek = n % 10
        n = n // 10
        sez.append(ostanek)
    sez.append(n)
    return sez[::-1]

print(sum(naredi_seznam(factorial(100))))
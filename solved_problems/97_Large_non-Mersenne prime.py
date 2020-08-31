# The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

# Find the last ten digits of this prime number.

#-------------------------------------------------------------------

def seznam_cifer(n):
    sez = []
    while n > 9:
        ostanek = n % 10
        n = n // 10
        sez.append(ostanek)
    sez.append(n)
    return sez[::-1]

# n = 2
# a = 1
# while len(seznam_cifer(n)) < 10:
#     n *= 2
#     a += 1
# print(n)
# 1073741824
# print(a)
# 30

n = 1073741824
a = 30
while a < 7830457:
    n *= 2
    a += 1
    n = int(str(n)[-10:])
print(str(28433 * n + 1)[-10:])
#8739992577


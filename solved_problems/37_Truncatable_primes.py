# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

#----------------------------------------------------------------------
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False      
    return True

def remove_digit_from_left(n):
    return(int(str(n)[1:]))

def remove_digit_from_right(n):
    return(int(str(n)[:-1]))

def truncatable_from_left(n):
    if not isPrime(n):
        return False
    while n > 9:
        n = remove_digit_from_left(n)
        if not isPrime(n):
            return False
    if not isPrime(n):
        return False
    return True


def truncatable_from_right(n):
    if not isPrime(n):
        return False
    while n > 9:
        n = remove_digit_from_right(n)
        if not isPrime(n):
            return False
    if not isPrime(n):
        return False
    return True

sez = []
n = 11
while len(sez) < 11:
    if truncatable_from_right(n) and truncatable_from_left(n):
        sez.append(n)
    n += 2
print(sum(sez))


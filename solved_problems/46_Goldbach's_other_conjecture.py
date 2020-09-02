# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

#---------------------------------------------------------------------------------

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False      
    return True

def primes_below(n):
    numbers = set(range((n - 1), 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def is_goldbach(n):
    if isPrime(n):
        return True
    for i in primes_below(n):
        possible_square = (n - i) / 2
        number = int(possible_square**(1/2))
        if (n - i) % 2 == 0 and ((number**2) == possible_square):
            return True
    return False

sez = []
n = 33
while len(sez) < 1:
    t = is_goldbach(n)
    if not is_goldbach(n):
        sez.append(n)
    n += 2
print(n - 2)




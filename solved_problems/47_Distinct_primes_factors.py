# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

#----------------------------------------------------------------
# def primes_below(n):
#     numbers = set(range(n, 1, -1))
#     primes = []
#     while numbers:
#         p = numbers.pop()
#         primes.append(p)
#         numbers.difference_update(set(range(p*2, n+1, p)))
#     return primes

#a bit too slow, will use other method

# def number_of_prime_factors(n):
#     factors = set()
#     for i in primes_below(n):
#         if n % i == 0:
#             factors.add(i)
#     return len(factors)
    

def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)


#the smallest possible number
j = 2*3*5*7

while True:
    if npf(j) == 4:
        j += 1
        if npf(j) == 4:
            j += 1
            if npf(j) == 4:
                j += 1
                if npf(j) == 4:
                    print(j-3)
                    break
    j += 1
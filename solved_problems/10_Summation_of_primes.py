# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

#------------------------------------------------------------------

# This method is super slow(the usage of Sieve of Eratosthenes is pretty bad)
#Below is optimized version

# def is_prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n % i==0:
#             return False
#     return True

# def multiples_below_n(a, n):
#     lis = [a]
#     m = 2
#     while m * a < n:
#         lis.append(m * a)
#         m += 1
#     return lis


# def list_of_primes_below(n):
#     all_numbers = [i for i in range(3,n, 2)]
#     primes = [2]
#     for i in all_numbers:
#         if is_prime(i):
#             primes.append(i)
#         for j in multiples_below_n(i, n):
#             if j in all_numbers:
#                 all_numbers.remove(j)
#     return primes
            

# print(sum(list_of_primes_below(2000000)))

#optimized Sieve od Eratosthenes
def sumPrimes(n):
    sum= 0
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print(sumPrimes(2000000))

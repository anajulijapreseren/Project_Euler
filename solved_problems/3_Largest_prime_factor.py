#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def is_prime(n):

    sez = []

    for i in range(1, int(n + 1)):

        if n % i == 0:

            sez += [i]

    return len(sez) == 2


def largest_prime_factor(n):
    i = 2
    while i <= n:
        if is_prime(i):
            if n % i == 0:
                n = (n / i)
                a = i
            else:
                i += 1
        else: 
            i += 1
    return a
            
print(largest_prime_factor(600851475143))
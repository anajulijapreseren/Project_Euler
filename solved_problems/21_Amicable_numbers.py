# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

#----------------------------------------------------------------
def sum_of_divisors_under(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


def amicable_numbers(n):
    amicable_sez = []
    sez = [i for i in range(2,n)]
    for i in sez:
        potential_friend = sum_of_divisors_under(i)

        if potential_friend < n and potential_friend != i and sum_of_divisors_under(potential_friend) == i:
            amicable_sez.append(i)
            amicable_sez.append(potential_friend)

    return amicable_sez

print((sum(set(amicable_numbers(10000)))))


# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

#----------------------------------------------------

# _ * _ _ _ = _ _ _ _ _not possible
# _ * _ _ _ _= _ _ _ _ OK
# _ _ * _ _ = _ _ _ _ _ not possible
# _ _* _ _ _ = _ _ _ _ OK

from itertools import permutations

perm = list(permutations([1,2,3,4,5,6,7,8,9]))

def make_numbers_form_list(lis, a, b):
    """changes list with 9 elements to numbers(by length): a, b, len - a - b"""
    num1 = ""
    num2 = ""
    num3 = ""
    sez = []
    i = 0
    while i < a:
        num1 += str(lis[i])
        i += 1
    sez.append(num1)
    while i < a + b:
        num2 += str(lis[i])
        i += 1
    sez.append(num2)
    while i < len(lis):
        num3 += str(lis[i])
        i += 1
    sez.append(num3)
    return sez
    
sett23 = set()
for permutation in perm:
    numbers = make_numbers_form_list(permutation, 2, 3)
    if int(numbers[0]) * int(numbers[1]) == int(numbers[2]):
        sett23.add(int(numbers[2]))

sett14 = set()
for permutation in perm:
    numbers = make_numbers_form_list(permutation, 1, 4)
    if int(numbers[0]) * int(numbers[1]) == int(numbers[2]):
        sett14.add(int(numbers[2]))

#sum is:
print(sum(sett14) + sum(sett23))

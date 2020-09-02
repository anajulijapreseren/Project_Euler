# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

#-----------------------------------------------------------------------
# slovar = {}
# for p in range(4, 1001):
#     solutions = set(    )
#     for c in range(1, p - 2):
#         for b in range(1, c):
#             a = p - c - b
#             if a < c and c**2 == a**2 + b**2:
#                 solutions.add({a, b, c})
#     slovar[p] = solutions
# print(slovar)

def combinations_of_3_numbers_to_make(n):
    combinations = []
    for c in range(1, n - 1):
        for b in range(1, c):
            a = n - b - c
            if a > 0 and a < b:
                if c**2 == b**2 + a**2:
                    combinations.append([c, b, a])
    return combinations

slovar = {}
for p in range(6, 1001):
    slovar[p] = len(combinations_of_3_numbers_to_make(p))
inverse = [(value, key) for key, value in slovar.items()]
print(sorted(inverse)[-1])
#(8, 840)--> answer is 840 (but it takes a lot of time)






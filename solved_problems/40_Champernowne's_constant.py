# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

#---------------------------------------------------------------------

#quick but ugly

n = 22
number = str(123456789101112131415161718192021)
while len(number) < 1000000:
    number += str(n)
    n += 1
print(int(number[0]) * int(number[9]) * int(number[99]) * int(number[999]) * int(number[9999]) * int(number[99999]) * int(number[999999]) )
# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest 
# recurring cycle in its decimal fraction part.

#we can see even d is definitely not the answer

def divide(a, b):
  '''Returns the decimal representation of the fraction a / b in three parts:
  integer part, non-recurring fractional part, and recurring part.'''
  assert b > 0
  integer = a // b
  remainder = a % b
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while(True):  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // b)
    remainder = remainder % b
    if remainder in seen:  # Digits have begun to recur.
      where = seen[remainder]
      return [integer, digits[:where], digits[where:]]
    else:
      seen[remainder] = len(digits)

def make_numbers_form_list(lis):
    """changes list to number"""
    num = ""
    i = 0
    while i < len(lis):
        num += str(lis[i])
        i += 1
    return int(num)


n = 0
max_digits = 0
for i in range(3, 1001, 2):
    if len(divide(1, i)[2]) > max_digits:
        n = i
        max_digits = len(divide(1, i)[2])
print(n)
